import pandas as pd
import csv
from datetime import datetime
from pathlib import Path
import os

# Insert this function after the imports (near the top of the file)

def collect_grades():
    """
    Interactively collect subject-grade pairs from the user,
    return a pandas DataFrame with columns ['Subject', 'Grade'].
    """
    rows = []
    print("\nWrite the subjects you course and the grades of each one. Leave the input(subject) empty to finish editing.")
    while True:
        subject = input("Subject: ").strip()
        if not subject:
            break
        grade_str = input(f"Grade for '{subject}' (0-100): ").strip()
        try:
            grade = float(grade_str)
            if grade < 0 or grade > 100:
                print("The grade must be between 0 and 100. Please try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number (e.g., 88 or 95.5).")
            continue
        rows.append({"Subject": subject, "Grade": grade})

    if not rows:
        print("No grades were entered.")
        return pd.DataFrame(columns=["Subject", "Grade"])

    df = pd.DataFrame(rows, columns=["Subject", "Grade"])
    print("\nGrade Table:")
    print(df.to_string(index=False))
    avg = df["Grade"].mean()
    print(f"Average: {avg:.2f}")

    save = input("Do you want to save this table to 'grades.csv'? (y/n): ").strip().lower()
    if save in ("y", "yes"):
        df.to_csv("grades.csv", index=False)
        print("Saved to 'grades.csv'.")

    return df

print("\033[1;33mWelcome to BUILD YOUR OWN PATH! \nLet's start by creating your profile.\n\033[0m")


# Building user profile
import os
import pandas as pd  

# Your original setup
script_dir = os.path.dirname(__file__) 
file_path = os.path.join(script_dir, 'users.csv') 

# If the file doesn't exist yet, create it
if not os.path.exists(file_path):
    df = pd.DataFrame(columns=["username", "password"])
    df.to_csv(file_path, index=False)

# Load the CSV file
users = pd.read_csv(file_path)

# Start message
start = str(input("Welcome to Build Your Own Path! Log in to Start: ")) 

# Ask for login info
username = str(input("Enter your username: ")) 
password = str(input("Enter your password: "))  

# Check if username and password exist
user_data = users[(users["Username"] == username) & (users["Password"] == password)]

if not user_data.empty:
    print(f"Welcome back, {username}!")

else:
    print("Username or password not found.")
    choice = input("Would you like to create a new account? (yes/no): ").lower()

    if choice == "yes":
        # Create new account
        new_username = input("Enter a new username: ")

        # Make sure the username doesn’t already exist
        while new_username in users["Username"].values:
            print("That username already exists. Please choose another.")
            new_username = input("Enter a new username: ")

        new_password = input("Enter a new password: ")

        # Add new user to the dataframe
        new_user = pd.DataFrame([[new_username, new_password]], columns=["username", "password"])
        users = pd.concat([users, new_user], ignore_index=True)

        # Save to CSV
        users.to_csv(file_path, index=False)

        print("You have created your username successfully!\n")

        # Ask them to log in again
        print("Please log in now.")
        username = str(input("Enter your username: ")) 
        password = str(input("Enter your password: "))  

        # Verify again
        user_data = users[(users["username"] == username) & (users["password"] == password)]
        if not user_data.empty:
            print(f"Welcome back, {username}!")
        else:
            print("Something went wrong. Try again later.")
    else:
        print("Goodbye!")
        
while True:
    # Validate name: must not be empty, must not contain digits, and must not be a single letter
    while True:
        name = input("\033[1;37mEnter your name:\033[0m ").strip()
        if not name:
            print("\033[1;31mName cannot be empty. Please enter your name.\033[0m")
            continue
        if any(char.isdigit() for char in name):
            print("\033[1;31mName cannot contain numbers. Please enter a valid name.\033[0m")
            continue
        # Require at least two alphabetic characters (prevents single-letter names like "A")
        if sum(1 for ch in name if ch.isalpha()) < 2:
            print("\033[1;31mName must contain at least two letters. Please enter your full name.\033[0m")
            continue
        break
   # Validate birthday: must match DD-MM-YYYY and be a real date (no future dates)
    while True:
        birthday_input = input("\033[1;37mEnter your birthday (DD-MM-YYYY): \033[0m").strip()
        try:
            birthday_dt = datetime.strptime(birthday_input, "%d-%m-%Y")
            if birthday_dt > datetime.now():
                print("\033[1;31mBirthday cannot be in the future. Please enter a valid date.\033[0m")
                continue
            elif datetime.now().year - birthday_dt.year > 70:
                print("\033[1;31mPlease enter a valid date.\033[0m")
                continue
            birthday = birthday_input
            break
        except ValueError:
            print("\033[1;31mInvalid date or format. Use DD-MM-YYYY (e.g., 31-12-2000).\033[0m")
    location = input("\033[1;37mEnter your location: \033[0m")
    highschool = input("\033[1;37mAre you in high school? (yes/no): \033[0m").strip().lower()
    # This will improve recommendations for the user depending on wether they are in high school or not
    if highschool in ("yes", "y"):
        highschool = "yes"
    else:
        highschool = "no"

    if highschool == "yes":
        semester = input( "What semester are you in? (e.g., 1st, 2nd, 3rd, etc.): ")
        # Grade average calculation for feedback on academic performance
        grade_stu = collect_grades()
        avg_grade = grade_stu["Grade"].mean() if not grade_stu.empty else 0.0
        print("Grade average: ", avg_grade)
        if avg_grade < 70: 
            print ("Student with bad grades, must present PAA") 
        elif avg_grade >= 70 and avg_grade <= 80: 
            print ("Regular student, can request Alizanza azul scholarship presenting PAA")
        elif avg_grade > 80 and avg_grade <= 90:
            print ("Student with good grades, can request Aliazan azul scholarship presenting PAA")
        elif avg_grade > 90 and avg_grade <= 100:
            print ("Excelent student, can request Excelencia academica and Aliza azul scholarships")

    def main():
        print("Here is a guide to study for PAA")
        choice = input("Do you want the guide link displayed? (yes/no): ").strip().lower()
        if choice in ("yes", "y"):
            url = "https://paa.aprendolibre.com/landing"
            print("Guide URL:", url)
            print("Copy and paste it into your browser when you're ready.")
        else:
            print("No guide will be shown.")
    if __name__ == "__main__":
        main()

    # Area of interest selection
    interest_list = ["Negocios", "Salud", "Estudios Creativos", "Ambiente Construido", "Derecho, Economia y Relaciones Internacionales", "Innovacion y Transformacion", "Computacion y Tecnologias de Informacion", "Bioingenieria y Procesos Quimicos", "Ciencias Aplicadas"]
    print("\n\033[1;37mSelect your area of interest from the list below (separate multiple choices with commas): \033[0m")
    for idx, interest in enumerate(interest_list, 1):
        print(f"{idx}. {interest}")

    while True:
    interest_input = input("Enter the numbers corresponding to your interests (e.g., 1,3): ")
    selected_interest = []
    for num in interest_input.split(","):
        num = num.strip()
        if num.isdigit():
            idx = int(num) - 1
            if 0 <= idx < len(interest_list):
                selected_interest.append(interest_list[idx])
    if selected_interest:
        break
    print("\033[1;31mInvalid input. Please enter valid numbers.\033[0m")
    
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
