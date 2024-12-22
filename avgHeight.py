student_height = input("Input a list of student heights : ").split()
for n in range(0, len(student_height)):
    student_height[n] = int(student_height[n])
print(student_height)

# sum
totalheight = 0
for height in student_height:
    totalheight += height

# lenght of list
no_of_stud = 0
for students in student_height:
    no_of_stud += 1

average_height = round(totalheight / no_of_stud)
print(average_height)
# totalheight=sum(student_height)
# no_of_stud=len(student_height)
# avg_height=round(total_height/no_of_stud)
# print(avg_height)
