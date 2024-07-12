import statistics

def isInvalid(score):
    return  float(score) > 100 or float(score) < 0

def getGrade(averagescore, attendance):
    attendance = float(attendance)
    if attendance < 75 or averagescore < 40:
        return "F"
    elif 55 > averagescore >= 40:
        return "D"
    elif 70 > averagescore >= 55:
        return "C"
    elif 85 > averagescore >= 70:
        return "B"
    elif 100 >= averagescore >= 85:
        return "A"
    
def getGPA(averagescore):
    return round(((averagescore*4)/100),2)

def getInitial(name):
    return name[0].upper()

print("Grade Calculator\n")

print("Student Details\n")

student_firstname = input("Enter your first name: ")
student_middlename = input("Enter your middle name: ")
student_lastname = input("Enter your last name: ")

print("\nStudent Scores and Attendance out of 100 \n")

student_score1 = input("Enter the student score 1: ")
student_score2 = input("Enter the student score 2: ")
student_score3 = input("Enter the student score 3: ")
student_attendance = input("Enter the student attendance percentage: ")

isTrueScore1 = isInvalid(student_score1)
isTrueScore2 = isInvalid(student_score2)
isTrueScore3 = isInvalid(student_score3)
isTrueAttendance = isInvalid(student_attendance)

while(isTrueScore1):
    print("\nYou have registered a incorrect value in the score 1. Please register the correct value.\n")
    student_score1 = input("Enter the student score 1: ")
    isTrueScore1 = isInvalid(student_score1)
    if(not isTrueScore1):
        print("Thanks for correcting the value!\n")

while(isTrueScore2):
    print("\nYou have registered a incorrect value in the score 2. Please register the correct value.\n")
    student_score2 = input("Enter the student score 2: ")
    isTrueScore2 = isInvalid(student_score2)
    if(not isTrueScore2):
        print("Thanks for correcting the value!")

while(isTrueScore3):
    print("\nYou have registered a incorrect value in the score 3. Please register the correct value.\n")
    student_score3 = input("Enter the student score 3: ")
    isTrueScore3 = isInvalid(student_score3)
    if(not isTrueScore3):
        print("Thanks for correcting the value!\n")

while(isTrueAttendance):
    print("\nYou have registered a incorrect value in the attendance percentage. Please register the correct value.\n")
    student_attendance = input("Enter the student attendance percentage: ")
    isTrueAttendance = isInvalid(student_attendance)
    if(not isTrueAttendance):
        print("Thanks for correcting the value!\n")

scores = [float(student_score1), float(student_score2), float(student_score3)]
averageExam = round(statistics.mean(scores),2)
initialFirstName = getInitial(student_firstname)
initialLastName = getInitial(student_middlename)
gradeStudent = getGrade(averageExam, student_attendance)
gpaStudent = getGPA(averageExam)

print("\nResults:\n\n")
print("Student: ", initialFirstName+initialLastName," ", student_lastname.upper(), "\n")
print("Average Score Exam: ", averageExam, "\n")
print("Overall Grade: ", gradeStudent, "\n")
print("GPA: ", gpaStudent, "\n")