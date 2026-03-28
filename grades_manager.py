student_grades = {
    "Alice": {
        "Math": 90.5,
        "English": 85.0,
        "Science": 92.0
    },
    "Bob": {
        "Math": 78.0,
        "English": 82.5,
        "History": 88.0
    },
    "Charlie": {
        "Science": 95.0,
        "English": 89.5
    }
}

def initialize_dict(student_name, subject_grades):
    return {student_name: subject_grades}

def add_student(student_grades=None):
    if student_grades is None:
        student_grades = {}
    
    student_name = input("Enter student name: ").strip().title()

    subjects = {}
    while True:
        entry = input("Enter subject and grade (or 'exit' to finish): ").strip()
        if entry.lower() == "exit":
            break
        
        grade_str = input(f"Enter grade for {subject}: ").strip()

        if grade_str.replace(".", "", 1).isdigit():
            grade = float(grade_str)
            subjects[subject.title()] = grade
        else:
            print("Grade must be numeric. Try again.")

    student_grades[student_name] = subjects
    print(f"Student {student_name} successfully added to the grades management system.")
    return student_grades

def get_students(student_grades, keys):
   
    result = {}

    lower_map = {name.lower(): name for name in student_grades.keys()}

    for key in keys:
        key_lower = key.lower()
        if key_lower in lower_map:  
            original_name = lower_map[key_lower]
            result[original_name] = student_grades[original_name]
        else:
            print(f"{key.title()} not found!")

    return result

def avg_by_student(student_grades, keys=None):
   
    if keys is None:
        selected = student_grades
    else:
        lower_map = {name.lower(): name for name in student_grades.keys()}
        selected = {}
        for key in keys:
            key_lower = key.lower()
            if key_lower in lower_map:
                original_name = lower_map[key_lower]
                selected[original_name] = student_grades[original_name]
            else:
                print(f"{key.title()} not found!")

    for student, grades in selected.items():
        if grades:
            avg = sum(grades.values()) / len(grades)
            print(f"{student}: {avg:.1f}")
        else:
            print(f"{student}: 0.0")