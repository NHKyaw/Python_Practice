user_name = input("Enter your username: ")
password = int(input("Enter your password: "))

if user_name == "admin" and password == 1234:
    print("Login Successful")
    role = input("Enter your role: ")
    if role == "teacher":
        number_of_students = int(input("Enter number of students in the Class: "))
        print (f"Welcome, teacher. You are managing {number_of_students} students.")
    elif role == "student":
        fav_subjects = input("Enter favorite subjects: ")
        print(f"Hello student! Enjoy studying {fav_subjects}.")
    else:
        print("Unknown role. Access limited.")
else:
    print("Login Failed")
