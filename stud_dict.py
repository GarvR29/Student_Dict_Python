students = {}

while True:
    print("\t\t\t\t\t\tSTUDENT DICTIONARY PROGRAM")
    print("\t\t\t\t\t\t**************************")
    print("1. Add Student ")
    print("2. Remove Student ")
    print("3. Update Age ")
    print("4. Print Students ")
    print("5. Exit ")


    choice = int(input("Enter your choice : "))

    if choice == 1:
        name = input("Enter the student's name : ")
        age = int(input("Enter the student's age :"))
        students.update({name : age})
        print(f"Student {name} added successfully!!\n")
    
    elif choice == 2:
        delete = input("Enter the name of the student to remove from the dictionary : ")  
        del students[delete]
        print(f"Student removed successfully!!\n")
    
    elif choice == 3:
        changed_name = input("Enter student name : ")
        if changed_name in students:
            new_age = int(input("Enter the new age : "))
            students.update({changed_name : new_age})
            print(f"Student age updated succesfully!!\n")   
        else:
            print("Student Not Found !!")   
        
    
    elif choice == 4:
        print("Student List :- \n")
        for x, y in students.items():
            print(x,":",y,"\n")
    
    elif choice == 5:
        break
    
    else:
        print("Invalid Choice. Please choose again.")
