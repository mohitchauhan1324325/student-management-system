from sqlalchemy.orm import Session
import models, schemas

def get_students(db: Session):
    return db.query(models.Student).all()

def add_student(db: Session, student: schemas.StudentCreate):
    db_student = models.Student(**student.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def delete_student(db: Session, student_id: int):
    student = db.query(models.Student).get(student_id)
    if student:
        db.delete(student)
        db.commit()
        return True
    return False
