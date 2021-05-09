class students_mangement:

    # constructor
    def __init__(self, student_full_name, student_ID, student_major, student_course, student_grade, student_course2,
                 student_grade2, student_course3, student_grade3):
        self.student_full_name = student_full_name
        self.student_ID = student_ID
        self.student_major = student_major
        self.student_course = student_course
        self.student_grade = student_grade
        self .student_course2 = student_course2
        self.student_grade2 = student_grade2
        self.student_course3 = student_course3
        self.student_grade3 = student_grade3

    # a function to display all the student information
    def show(self, ob):
        print("student full name  : ", ob.student_full_name)
        print("student ID : ", ob.student_ID)
        print("student major : ", ob.student_major)
        print("student course : ", ob.student_course)
        print("student grade : ", ob.student_grade)
        print("student course2 :", ob.student_course2)
        print("student grade2 : ", ob.student_grade2)
        print("student course3 :", ob.student_course3)
        print("student grade3 : ", ob.student_grade3)
        print("\n")

    # a function to add more students
    def add(self, student_full_name, student_ID, student_major, student_course, student_grade, student_course2,
            student_grade2, student_course3, student_grade3):
        ob = students_mangement(student_full_name, student_ID, student_major, student_course, student_grade,
                                student_course2, student_grade2, student_course3, student_grade3)
        list.append(ob)

    # a function to search for student information
    def search(self, student_full_name, student_ID, student_major, student_course, student_grade, student_course2,
               student_grade2, student_course3, student_grade3):
        for i in range(list.__len__()):
            if list[i].student_full_name == student_full_name:
                return i
            elif list[i].student_ID == student_ID:
                return i
            elif list[i].student_major == student_major:
                return i
            elif list[i].student_course == student_course:
                return i
            elif list[i].student_grade == student_grade:
                return i
            elif list[i].student_course2 == student_course2:
                return i
            elif list[i].student_grade2 == student_grade2:
                return i
            elif list[i].student_course3 == student_course3:
                return i
            elif list[i].student_grade3 == student_grade3:
                return i

    # a function to update student information
    def update(self, student_name, new_student_full_name, ID, new_student_ID, major, new_major, course, new_course,
               student_grade, new_grade, student_course2, new_student_course2, student_grade2, new_student_grade2,
               student_course3, new_student_course3, student_grade3, new_student_grade3):
        students_name = obj.search(student_name, student_name, student_name, student_name, student_name, student_name,
                             student_name, student_name, student_name)
        list[students_name].student_full_name = new_student_full_name

        Id = obj.search(ID, ID, ID, ID, ID, ID, ID, ID, ID)
        list[Id].student_ID = new_student_ID

        Major = obj.search(major, major, major, major, major, major, major, major, major)
        list[Major].student_major = new_major

        Course = obj.search(course, course, course, course, course, course, course, course, course)
        list[Course].student_course = new_course

        Grade = obj.search(student_grade, student_grade, student_grade, student_grade, student_grade,
                           student_grade, student_grade, student_grade, student_grade)
        list[Grade].student_grade = new_grade

        Student_course2 = obj.search(student_course2, student_course2, student_course2, student_course2,
                                     student_course2, student_course2, student_course2, student_course2,
                                     student_course2)
        list[Student_course2].student_course2 = new_student_course2

        Grade2 = obj.search(student_grade2, student_grade2, student_grade2, student_grade2, student_grade2,
                            student_grade2, student_grade2, student_grade2, student_grade2)
        list[Grade2].student_grade2 = new_student_grade2

        Student_course3 = obj.search(student_course3, student_course3, student_course3, student_course3,
                                     student_course3, student_course3, student_course3, student_course3,
                                     student_course3)
        list[Student_course3].student_course3 = new_student_course3
        Grade3 = obj.search(student_grade3, student_grade3, student_grade3, student_grade3, student_grade3,
                            student_grade3, student_grade3, student_grade3, student_grade3)
        list[Grade3].student_grade3 = new_student_grade3

    # a function to delete a student information
    def delete(self, student_name, ):
        students_name = obj.search(student_name, student_name, student_name, student_name, student_name, student_name,
                                   student_name, student_name, student_name)
        del list[students_name]

        def l(ID):
            Id = obj.search(ID, ID, ID, ID, ID, ID, ID, ID, ID)
            del list[Id]


list = []

obj = students_mangement("", "", "", "", 0, "", 0, "", 0)
obj.add(input("student full name : "), input("student ID : "), input("student major : "), input("student courses :"),
        float(input("student grades : ")), input("student_course 2 : "), float(input("student grade 2 : ")),
        input("student course 3 :", ), float(input("student Grade 3 :")))
while True:
    print('''what would you like to do ? 
    1 - show all the student.
    2 - add a student.
    3 - update a student information.
    4 - search for a student. 
    5 - delete a student.''')

    choose = float(input("Enter a number : "))
    if choose == 1:
        for i in range(list.__len__()):
            obj.show(list[i])
    elif choose == 2:

        student_name = input("Enter the student full name : ")
        ID = input("Enter the student ID : ")
        student_major = input("Enter the student major : ")
        student_course = input("Enter the student wcourse : ")
        student_grade = float(input("Enter student grade : "))
        student_course2 = input("Enter student course2 : ")
        student_grade2 = float(input("Enter student grade2 :"))
        student_course3 = input("Enter student course3 :")
        student_grade3 = float(input("Enter student grade3 :"))
        obj.add(student_name, ID, student_major, student_course, student_grade, student_course2, student_grade2,
                student_course3, student_grade3)
        for i in range(list.__len__()):
            obj.show(list[i])
    elif choose == 3:
        print('''what would you like to do ? 
           1 - update a student name .
           2 - update a student ID .
           3 - update a student major.
           4 - update student course (1,2,3). 
           5 - update student grade((1,2,3).''')
        up2 = input("what would you like to update ?")
        if up2 == "1":

            student_name = input("Enter student name : ")
            new_student_full_name = input("Enter the student name after change : ")
            students_name = obj.search(student_name, student_name, student_name, student_name, student_name,
                                       student_name,
                                       student_name, student_name, student_name)
            list[students_name].student_full_name = new_student_full_name

            for i in range(list.__len__()):
                obj.show(list[i])
        elif up2=="2":

                ID = input("Enter student ID :")
                new_student_ID = input("Enter new student ID :")
                Id = obj.search(ID, ID, ID, ID, ID, ID, ID, ID, ID)
                list[Id].student_ID = new_student_ID
                for i in range(list.__len__()):
                    obj.show(list[i])
        elif up2=="3":

            major = input("Enter major : ")
            new_major = input("Enter new major :")
            Major = obj.search(major, major, major, major, major, major, major, major, major)
            list[Major].student_major = new_major
            for i in range(list.__len__()):
                obj.show(list[i])
        elif up2=="4":

            Q7=input("what course would you like to change?(1,2,3) ")
            if Q7 =="1":
                    course = input("Enter course :")
                    new_course = input("Enter new course : ")
                    Course = obj.search(course, course, course, course, course, course, course, course, course)
                    list[Course].student_course = new_course
                    for i in range(list.__len__()):
                        obj.show(list[i])
            elif Q7=="2":
                student_course2 = input("Enter course2 :")
                new_student_course2 = input("Enter new course 2 :")
                Student_course2 = obj.search(student_course2, student_course2, student_course2, student_course2,
                                             student_course2, student_course2, student_course2, student_course2,
                                             student_course2)
                list[Student_course2].student_course2 = new_student_course2
                for i in range(list.__len__()):
                    obj.show(list[i])
            elif Q7=="3":
                student_course3 = input("Enter course3 : ")
                new_student_course3 = input("Enter new course3 :")
                Student_course3 = obj.search(student_course3, student_course3, student_course3, student_course3,
                                             student_course3, student_course3, student_course3, student_course3,
                                             student_course3)
                list[Student_course3].student_course3 = new_student_course3
                for i in range(list.__len__()):
                    obj.show(list[i])

        elif up2=="5":
            Q8=input("What student grade would you like to change ? (1,2,3")
            if Q8=="1":
                student_grade = float(input("Enter grade : "))
                new_student_grade = float(input("Enter new grade : "))
                Grade = obj.search(student_grade, student_grade, student_grade, student_grade, student_grade,
                                   student_grade, student_grade, student_grade, student_grade)
                list[Grade].student_grade =  new_student_grade
                for i in range(list.__len__()):
                    obj.show(list[i])
            elif Q8=="2":
                student_grade2 = float(input("Enter grade 2 :"))
                new_student_grade2 = float(input("Enter new grade 2 : "))
                Grade2 = obj.search(student_grade2, student_grade2, student_grade2, student_grade2, student_grade2,
                                    student_grade2, student_grade2, student_grade2, student_grade2)
                list[Grade2].student_grade2 = new_student_grade2
                for i in range(list.__len__()):
                    obj.show(list[i])
            elif Q8=="3":
                student_grade3 = float(input("Enter grade3 :"))
                new_student_grade3 = float(input("Enter new grade3 :"))
                Grade3 = obj.search(student_grade3, student_grade3, student_grade3, student_grade3, student_grade3,
                                    student_grade3, student_grade3, student_grade3, student_grade3)
                list[Grade3].student_grade3 = new_student_grade3
                for i in range(list.__len__()):
                    obj.show(list[i])

    elif choose == 4:
        while True:
            Q2 = input(
                "Enter (name) if you want to search by student full name  . or Enter  (ID) : if you want to search by student ID : ")
            if Q2 == "name":
                student_name = input("Enter student name : ")
                look = obj.search(student_name, student_name, student_name, student_name, student_name, student_name,
                                  student_name, student_name, student_name)
                obj.show(list[look])
                break
            elif Q2 == "ID":
                ID = input(" Enter student ID : ")
                look = obj.search(ID, ID, ID, ID, ID, ID, ID, ID, ID)
                obj.show(list[look])
                break
            else:
                print("Enter (name/ID)")


    elif choose == 5:
        while True:
            Q3 = input(
                "Enter (name) if you want to delete by student full name  . or Enter  (ID) : if you want to delete by student ID : ")
            if Q3.lower() == "name":

                student_name = input("Enter name : ")

                obj.delete(student_name)
                print(list.__len__())
                for i in range(list.__len__()):
                    obj.show(list[i])
                break
            elif Q3.upper() == "ID":
                ID = input("Enter ID ")
                obj.delete(ID)
                print(list.__len__())
                for i in range(list.__len__()):
                    obj.show(list[i])
                break
            else:
                print("Enter(name/ID)")
    while True:
        Q5 = input("would you like to do another task ? (yes/no) ")
        if Q5.lower() == "no":
            exit()
        elif Q5.lower() == "yes":
            break
        else:
            print("Enter (yes,no)")
