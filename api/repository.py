from api.database import Database


class Repository():
    def __init__(self) -> None:
        self.database = Database()

    def createStudentRecord(self, student):
        if self.database.create(student):
            return {"msg": "Created"}
        return {"error": "Error creating student record!"}

    def getAllStudentRecord(self):
        return {"students": self.database.fetchAllStudents()}

    def updateStudentRecord(self, student):
        studentRecord = self.database.fetchStudent(student.studentId)
        if studentRecord is None:
            return {"error": "Student not found"}
        else:
            if self.database.update(student):
                return {"msg": "Updated"}
            return {"error": "Error updating student record!"}

    def deleteStudentRecord(self, studentId):
        studentRecord = self.database.fetchStudent(studentId)
        if studentRecord is None:
            return {"error": "Student not found"}
        else:
            if self.database.delete(studentId):
                return {"msg": "Deleted"}
            return {"error": "Error deleting student record!"}
