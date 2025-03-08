from flask import jsonify
from models import Student, Teacher, Grade, Semester
from routes.api_blueprint import api_bp

@api_bp.route('/students/cgpa-timeframe/<string:start_sem>/<string:end_sem>', methods=['GET'])
def get_students_cgpa_timeframe(start_sem, end_sem):
    students = Student.query.all()

    students_list = []
    for s in students:
        start_sem_obj = Semester.query.filter_by(semester_name=start_sem).first()
        end_sem_obj = Semester.query.filter_by(semester_name=end_sem).first()
        teacher_name = Teacher.query.with_entities(Teacher.name).filter_by(id=s.teacher_id).first()[0]
        
        # Filter grade based on timeframe
        grades = Grade.query.filter(
            (Grade.student_id == s.id) & 
            (Grade.semester_id >= start_sem_obj.id) &
            (Grade.semester_id <= end_sem_obj.id)
        )
        
        cgpa = round(sum(grade.gpa for grade in grades) / grades.count(), 2)
        # Append dict to list
        students_list.append({
            "Name": s.name,
            "Teacher's Name": teacher_name,
            "cGPA": cgpa
        })
    return jsonify(students_list)