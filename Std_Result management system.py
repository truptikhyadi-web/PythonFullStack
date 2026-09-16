name=input("Enter your name:")
course=input("ENter your course:")
Subjects=("python","java","maths","english","c#")
marks=[]
for subject in Subjects:
    mark=int(input("Enter marks in " + subject + ":"))
    marks.append(mark)
student={
    "Name":name,
    "course":course,
    "Subjects":Subjects,
    "Marks":marks
    }
total=sum(marks)
highest=max(marks)
lowest=min(marks)
num_of_Subjects=len(marks)
percentage=total/num_of_Subjects
if percentage >= 90:
    Grade="A+"
elif percentage >= 80:
    Grade="A"
elif percentage >= 70:
    Grade="B"
elif percentage >= 60:
    Grade="C"
elif percentage >= 50:
    Grade="D"
else:
    Grade="Fail"
print("Name:",student["Name"])
print("Course:",student["course"])
print("Subjects:",student["Subjects"])
print("Marks:",student["Marks"])
print("Total Marks:",total)
print("Highest Mark:",highest)
print("Lowest Mark:",lowest)
print("Number of Subjects:",num_of_Subjects)
print("Percentage:",percentage)
print("Grade:",Grade)




      
      
            




    
    
