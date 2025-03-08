from flask import jsonify
from models import db, Student, Teacher
from routes.api_blueprint import api_bp


@api_bp.route('/students/<int:student_id>/reassign', methods=['PUT'])
def reassign_teacher(student_id):
    stud = Student.query.filter_by(id=student_id).first()
    other_teacher = Teacher.query.filter(Teacher.id != stud.teacher_id).first()
    stud.teacher_id = other_teacher.id
    db.session.commit()

    return jsonify({
        "message": "Student reassigned successfully",
        "student": stud.name,
        "updated_teacher": other_teacher.name
    })
