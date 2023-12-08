def gpa(score):

    if 80 <= score <= 100:
        grade = 'A+'
        points = 4.0
    elif 75 <= score < 79:
        grade = 'A'
        points = 3.75
    elif 70 <= score < 74:
        grade = 'A-'
        points = 3.50
    elif 65 <= score < 69:
        grade = 'B+'
        points = 3.25
    elif 60 <= score <64:
        grade = 'B'
        points = 3.0
    elif 55 <= score < 59:
        grade = 'B-'
        points= 2.75
    elif 50 <= score < 54:
        grade = 'C+'
        points = 2.50
    elif 45 <= score < 49:
        grade = 'C'
        points = 2.25
    elif 40 <= score < 44:
        grade = 'C-'
        points = 2.0
    elif 37 <= score < 44:
        grade = 'D'
        points =1
    else:
        grade = 'F'
        points = 0.0

    return grade, points

student = float(input("শিক্ষার্থীর নাম্বার ইনপুট দিন: "))

grade_result, points_result = gpa(student)
print(f"গ্রেড: {grade_result}, পয়েন্ট: {points_result}")
