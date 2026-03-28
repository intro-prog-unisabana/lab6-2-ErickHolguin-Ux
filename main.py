from grades_manager import add_student, avg_by_student

def main():
    print("Welcome to the Student Grades Manager!\n")
    my_grades = {}

    while True:
        print("Select an option:")
        print("1. Add a student")
        print("2. Print student grade averages")
        print("3. Exit\n")

        choice = input().strip()

        if choice == "1":
            my_grades = add_student(my_grades)

        elif choice == "2":
            print("\nSelect an option:")
            print("a. Display all students")
            print("b. Display selected students\n")

            sub_choice = input().strip().lower()

            if sub_choice == "a":
                avg_by_student(my_grades)

            elif sub_choice == "b":
                names = input("Enter student names (comma-separated):\n").strip()
                keys = [name.strip() for name in names.split(",") if name.strip()]
                avg_by_student(my_grades, keys)

            else:
                print("Invalid option selected!\n")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid option selected!\n")


if __name__ == "__main__":
    main()
