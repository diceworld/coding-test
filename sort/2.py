"""
학생의 이름과 성적정보가 주어졌을 때 성적이 낮은 순서대로 학생의 이름을 출력하시오.
"""
n = int(input())  # N
students = []  # 학생 리스트

for i in range(n):
    student = input().split()
    students.append((str(student[0]), int(student[1])))

students.sort(key=lambda x: x[1])

for student in students:
    print(student[0], end=' ')
