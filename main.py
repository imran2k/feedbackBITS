stdr= input("Enter your full Roll Number (eg: 18C31A0XXX):    ")
stdn= input("Enter your name in block letters (eg: ABDUL KALAAM):    ")
while True :
    stdbr =input("Enter your branch name: ")
    if stdbr == "CSE":
        print("--------------Computer Science Department----------------")
        print("Name:",(stdn))
        print("Roll Number:",(stdr))
        print("""Please note that each and every feedback recorded will be analyzed seriously so be honest with your rating!
        
              Rate """)

        crrate=input("Rate the maintainance of the classroom: ")
        ctrate=input("Rate the class teachers performance: ")
        hodrate=input("Rate the management of Head of Department: ")
        pnrate=input("Rate the punctuality of lecturers: ")
        syrate=input("Rate the syllabus management of lecturers: ")

    elif stdbr == "ECE":
        print("--------------Electronics & Communication Department----------------")
        print("Name:", (stdn))
        print("Roll Number:", (stdr))
        print("""Please note that each and every feedback recorded will be analyzed seriously so be honest with your rating!

                      Rate """)

        crrate = input("Rate the maintainance of the classroom: ")
        ctrate = input("Rate the class teachers performance: ")
        hodrate = input("Rate the management of Head of Department: ")
        pnrate = input("Rate the punctuality of lecturers: ")
        syrate = input("Rate the syllabus management of lecturers: ")

    elif stdbr == "Civil":
        print("--------------Civil Department----------------")
        print("Name:", (stdn))
        print("Roll Number:", (stdr))
        print("""Please note that each and every feedback recorded will be analyzed seriously so be honest with your rating!

                      Rate """)

        crrate = input("Rate the maintainance of the classroom: ")
        ctrate = input("Rate the class teachers performance: ")
        hodrate = input("Rate the management of Head of Department: ")
        pnrate = input("Rate the punctuality of lecturers: ")
        syrate = input("Rate the syllabus management of lecturers: ")

    elif stdbr == "Mechanical":
        print("--------------Mechanical Department----------------")
        print("Name:", (stdn))
        print("Roll Number:", (stdr))
        print("""Please note that each and every feedback recorded will be analyzed seriously so be honest with your rating!

                      Rate """)

        crrate = input("Rate the maintainance of the classroom: ")
        ctrate = input("Rate the class teachers performance: ")
        hodrate = input("Rate the management of Head of Department: ")
        pnrate = input("Rate the punctuality of lecturers: ")
        syrate = input("Rate the syllabus management of lecturers: ")

    elif stdbr == "EEE":
        print("--------------Electrical & Electronics Department----------------")
        print("Name:", (stdn))
        print("Roll Number:", (stdr))
        print("Please note that each and every feedback recorded will be analyzed seriously so be honest with your rating!")

        crrate = input("Rate the maintainance of the classroom: ")
        ctrate = input("Rate the class teachers performance: ")
        hodrate = input("Rate the management of Head of Department: ")
        pnrate = input("Rate the punctuality of lecturers: ")
        syrate = input("Rate the syllabus management of lecturers: ")

    else:
        print("Invalid Answer")
    break

print("Feedback recorded!")
print("Classroom maintainance:",(crrate),"/5")
print("Class teacher performance:",(ctrate),"/5")
print("HOD Management rating:",(hodrate),"/5")
print("Lecturers' Punctuality:",(pnrate),"/5")
print("Lecturers' syllabus management:",(syrate),"/5")



print("-------------Thank you------------------")










