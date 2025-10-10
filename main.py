print("\033[1;33mWelcome to BUILD YOUR OWN PATH! \nLet's start by creating your profile.\n\033[0m")

# Building user profile
while True:
    name = input("\033[1;37mEnter your name:\033[0m ")
    birthday = input("\033[1;37mEnter your birthday (DD-MM-YYYY): \033[0m")
    location = input("\033[1;37mEnter your location: \033[0m")
    highschool = input("\033[1;37mAre you in high school? (yes/no): \033[0m").strip().lower()
    if highschool in ("yes", "y"):
        highschool = "yes"
    else:
        highschool = "no"

    if highschool == "yes":
        semester = input( "What semester are you in? (e.g., 1st, 2nd, 3rd, etc.): ")
    grade_stu = pd.read_csv("grades.csv")
    avg_grade = (grade_stu["Grade"].mean())
    print("Grade average: ", avg_grade)
    if avg_grade < 70: 
        print ("Student with bad grades")
    elif avg_grade <= 80: 
        print ("Regular student")
    elif avg_grade <= 90:
        print ("Student with good grades")
    elif avg_grade <= 95:
        print ("Excelent student")

    # Area of interest selection
    interest_list = ["Negocios", "Salud", "Estudios Creativos", "Ambiente Construido", "Derecho, Economia y Relaciones Internacionales", "Innovacion y Transformacion", "Computacion y Tecnologias de Informacion", "Bioingenieria y Procesos Quimicos", "Ciencias Aplicadas"]
    print("\n\033[1;37mSelect your area of interest from the list below (separate multiple choices with commas): \033[0m")
    for idx, interest in enumerate(interest_list, 1):
        print(f"{idx}. {interest}")

    interest_input = input("Enter the numbers corresponding to your interests (e.g., 1,3): ")
    selected_interest = []
    for num in interest_input.split(","):
        num = num.strip()
        if num.isdigit():
            idx = int(num) - 1
            if 0 <= idx < len(interest_list):
                selected_interest.append(interest_list[idx])
    # Display user profile
    print("\n\033[1;33mUser Profile:\033[0m")
    print(f"Name: {name}")
    print(f"Birthday: {birthday}")
    print(f"Location: {location}")
    print(f"In High School: {highschool}")
    if highschool == "yes":
        print(f"Semester: {semester}")
    print(f"Areas of Interest: {', '.join(selected_interest) if selected_interest else 'None'}")

    # Option to redo profile
    print("\n\033[1;37mDo you want to make changes to your profile? (yes/no):\033[0m ")
    change_profile = input().strip().lower()
    if change_profile in ("yes", "y"):
        continue
    else:
        print("\n\033[1;33mProfile created successfully!\033[0m")
        break 
