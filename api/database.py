from sqlalchemy import create_engine, update
from sqlalchemy.orm import Session

from api.model.StudentRecord import StudentRecord


class Database():
    def __init__(self) -> None:
        self.session = self.connectDB()

    def connectDB(self):
        engine = create_engine(
            "mysql+pymysql://root_1:root_1@db_service/flask_assignment_db")
        return Session(bind=engine)

    def create(self, obj):
        self.session.add(obj)
        self.session.commit()
        return True

    def update(self, obj):
        student = self.session.query(StudentRecord).filter(
            StudentRecord.studentId == obj.studentId).one()
        if student:
            stmt = update(StudentRecord).\
                where(StudentRecord.studentId == obj.studentId).\
                values(firstName=obj.firstName,
                       lastName=obj.lastName,
                       dob=obj.dob,
                       amountDue=obj.amountDue)
            self.session.execute(stmt)
            self.session.commit()
            return True
        return False

    def delete(self, studentId):
        student = self.session.query(StudentRecord).filter(
            StudentRecord.studentId == studentId).one()
        if student:
            self.session.delete(student)
            self.session.commit()
            return True
        return False

    def fetchStudent(self, studentId):
        return self.session.query(StudentRecord).filter(StudentRecord.studentId == studentId).first()

    def fetchAllStudents(self):
        return self.session.query(StudentRecord).all()
