students = "DaySchollar" #Global Variable

def increaseStudent():
    global students
    students = "Interships_one" #Local Variable
    print(f"Total Student is: {students}")

increaseStudent()
print(f"Total Student is: {students}")
