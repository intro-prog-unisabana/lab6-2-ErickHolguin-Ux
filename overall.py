def student_averages(students):

    averages = {}
    for student_id, assignments in students.items():
        if assignments:
            avg = round(sum(assignments.values()) / len(assignments))
        else:
            avg = 0
        averages[student_id] = avg
    return averages


def assignment_averages(students):
    
    assignment_totals = {}
    assignment_counts = {}

    for student_id, assignments in students.items():
        for assignment, grade in assignments.items():
            assignment_totals[assignment] = assignment_totals.get(assignment, 0) + grade
            assignment_counts[assignment] = assignment_counts.get(assignment, 0) + 1

    averages = {}
    for assignment in assignment_totals:
        avg = round(assignment_totals[assignment] / assignment_counts[assignment])
        averages[assignment] = avg

    return averages