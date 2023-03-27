import json
from api.model.StudentRecord import StudentRecord
from api.model.StudentRecordEncoder import CustomJSONEncoder
from api.repository import Repository
from flask import Flask, request, jsonify, make_response

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "Flask Api Assignment"


@app.route('/student', methods=['POST'])
def createStudent():
    content = request.json
    if content["student_id"] is None:
        return jsonify({"error": "Student id is required"})
    student = StudentRecord(content["student_id"], content["first_name"],
                            content["last_name"], content["dob"], content["amount_due"])

    response = make_response(
        jsonify(Repository().createStudentRecord(student)), 201)
    response.headers['Content-Type'] = 'application/json'
    return response


@app.route('/student', methods=['PUT'])
def updateStudent():
    content = request.json
    if content["student_id"] is None:
        return jsonify({"error": "Student id is required"})
    student = StudentRecord(content["student_id"], content["first_name"],
                            content["last_name"], content["dob"], content["amount_due"])

    response = make_response(
        jsonify(Repository().updateStudentRecord(student)), 202)
    response.headers['Content-Type'] = 'application/json'
    return response


@app.route('/student/<student_id>', methods=['DELETE'])
def deleteStudent(student_id):
    if student_id is None:
        return jsonify({"error": "Student id is required"})

    response = make_response(
        jsonify(Repository().deleteStudentRecord(student_id)), 202)
    response.headers['Content-Type'] = 'application/json'
    return response


@app.route('/students', methods=['GET'])
def fetchStudents():
    records = Repository().getAllStudentRecord()
    response = make_response(json.dumps(records, cls=CustomJSONEncoder), 200)
    response.headers['Content-Type'] = 'application/json'
    return response


app.run(debug=True)
