from flask import jsonify
from models import Student, Teacher, Grade
from routes.api_blueprint import api_bp


@api_bp.route('/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    gpas = Grade.query.all()

    if not students:
        return jsonify({"error": "No students found"}), 404

    # {student.id: gpa}
    cgpa_dict = {} 
    for g in gpas:
        if g.student_id not in cgpa_dict:
            cgpa_dict[g.student_id] = 0
        cgpa_dict[g.student_id] += g.gpa

    students_list = []
    for s in students:
        teacher_name = Teacher.query.with_entities(Teacher.name).filter_by(id=s.teacher_id).first()[0]
        # {student.name: ___, teacher's name: ___, cgpa: ___}
        students_list.append({
            "Name": s.name,
            "Teacher's Name": teacher_name,
            "cGPA": round(cgpa_dict[s.id] / 8.0, 2)
        })
    return jsonify(students_list)