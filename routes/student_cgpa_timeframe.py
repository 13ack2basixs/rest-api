from flask import jsonify
from models import Student, Teacher, Grade, Semester
from routes.api_blueprint import api_bp

@api_bp.route('/students/cgpa-timeframe/<string:start_sem>/<string:end_sem>', methods=['GET'])
def get_students_cgpa_timeframe(start_sem, end_sem):
    students = Student.query.all()

    students_list = []
    for s in students:
        # Filter grade based on timeframe
        grades = Grade.query.filter(
            (Grade.student_id == s.id) & 
            (Grade.semester_id >= Semester.query.filter_by(semester_name=start_sem).first().id) &
            (Grade.semester_id <= Semester.query.filter_by(semester_name=end_sem).first().id)
        )
        
        cgpa = round(sum(grade.gpa for grade in grades) / grades.count(), 2)
        # Create dict for each student
        student_dict = {}
        student_dict["Name"] = s.name
        student_dict["Teacher's Name"] = Teacher.query.with_entities(Teacher.name).filter_by(id=s.teacher_id).first()[0]
        student_dict["cGPA"] = cgpa
        students_list.append(student_dict)
    return jsonify(students_list)