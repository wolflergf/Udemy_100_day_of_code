# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
print(student_heights)
total_height = 0
number_students = 0
# Write your code below this row 👇
for height in student_heights:
    total_height += height
    number_students += 1

total = total_height / number_students
print('{:.0f}'.format(total))
