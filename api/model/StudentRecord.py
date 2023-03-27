from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class StudentRecord(Base):
    __tablename__ = 'students'

    studentId = Column(Integer, primary_key=True)
    firstName = Column(String(50))
    lastName = Column(String(50))
    dob = Column(Date)
    amountDue = Column(Integer)

    def __init__(self, studentId, firstName, lastName, dob, amountDue):
        self.studentId = studentId
        self.firstName = firstName
        self.lastName = lastName
        self.dob = dob
        self.amountDue = amountDue

    def __repr__(self):
        return f"<StudentRecord(studentId={self.studentId}, firstName='{self.firstName}', lastName='{self.lastName}', dob='{self.dob}', amountDue={self.amountDue})>"
