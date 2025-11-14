import pandas as pd
import csv
from datetime import datetime
from pathlib import Path
import os
import json

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

print("\033[1;33mWelcome to BUILD YOUR OWN PATH!\033[0m")


""" Building user profile """
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

# Ensure profile columns exist so further code can read/write them safely
_profile_cols = ["name", "birthday", "location", "highschool", "semester", "interests"]
for col in _profile_cols:
    if col not in users.columns:
        users[col] = ""

# Start message
start = print("Log in to Start")

# LOGIN LOOP: repeat until valid credentials or new account creation
profile_exists = False
selected_interest = []
user_data = pd.DataFrame()  # ensure variable exists

while True:
    username = str(input("Enter your username: ")) 
    password = str(input("Enter your password: "))  

    # Check if username and password exist
    mask = (users["username"] == username) & (users["password"] == password)
    user_data = users[mask]

    if not user_data.empty:
        print(f"Welcome back, {username}!")
        break  # authenticated, proceed
    else:
        print("Username or password not found.")
        choice = input("Would you like to create a new account? (yes/no): ").lower()
        if choice in ("yes", "y"):
            # Create new account
            new_username = input("Enter a new username: ")

            # Make sure the username doesn’t already exist
            while new_username in users["username"].values:
                print("That username already exists. Please choose another.")
                new_username = input("Enter a new username: ")

            new_password = input("Enter a new password: ")

            # Add new user to the dataframe
            new_user = pd.DataFrame([[new_username, new_password]], columns=["username", "password"])
            users = pd.concat([users, new_user], ignore_index=True)

            # Save to CSV
            users.to_csv(file_path, index=False)

            print("You have created your username successfully! (please save your username and password in a safe place)")

            # set username/password to the created account and load its row
            username = new_username
            password = new_password
            mask = (users["username"] == username) & (users["password"] == password)
            user_data = users[mask]
            print("Logged in as the new user.")
            break  # proceed to collect profile for new user
        else:
            # user chose not to create an account -> go back to login prompt
            print("\nReturning to login. Please enter credentials again.\n")
            # re-print start message for clarity
            start = print("Log in to Start")
            continue

profile_exists = False
selected_interest = []

if not user_data.empty:
    # Try to read stored profile fields
    row = user_data.iloc[0]
    name_stored = str(row.get("name", "")).strip()
    if name_stored and name_stored.lower() not in ("nan", ""):
        # consider profile present if name is stored
        profile_exists = True
        name = name_stored
        birthday = str(row.get("birthday", "")).strip()
        location = str(row.get("location", "")).strip()
        highschool = str(row.get("highschool", "")).strip().lower() or "no"
        semester = str(row.get("semester", "")).strip()
        interests_raw = row.get("interests", "")
        try:
            if isinstance(interests_raw, str) and interests_raw.strip():
                selected_interest = json.loads(interests_raw)
            else:
                selected_interest = []
        except Exception:
            # fallback: try to parse as comma separated
            selected_interest = [s.strip() for s in str(interests_raw).split(",") if s.strip()]

        # Display stored profile and skip asking for profile again
        print("\n\033[1;33mStored User Profile:\033[0m")
        print(f"Name: {name}")
        print(f"Birthday: {birthday}")
        print(f"Location: {location}")
        print(f"In High School: {highschool}")
        if highschool == "yes" and semester:
            print(f"Semester: {semester}")
        print(f"Areas of Interest: {', '.join(selected_interest) if selected_interest else 'None'}")
    else:
        # No profile saved yet; will prompt below to collect profile
        profile_exists = False

else:
    print("Username or password not found.")
    choice = input("Would you like to create a new account? (yes/no): ").lower()

    if choice in ("yes", "y"):
        # Create new account
        new_username = input("Enter a new username: ")

        # Make sure the username doesn’t already exist
        while new_username in users["username"].values:
            print("That username already exists. Please choose another.")
            new_username = input("Enter a new username: ")

        new_password = input("Enter a new password: ")

        # Add new user to the dataframe
        new_user = pd.DataFrame([[new_username, new_password]], columns=["username", "password"])
        users = pd.concat([users, new_user], ignore_index=True)

        # Save to CSV
        users.to_csv(file_path, index=False)

        print("You have created your username successfully! (please save your username and password in a safe place)")

        # Ask them to log in again
        print("Please log in now.")
        username = str(input("Enter your username: ")) 
        password = str(input("Enter your password: "))  

        # Verify again
        mask = (users["username"] == username) & (users["password"] == password)
        user_data = users[mask]
        if not user_data.empty:
            print(f"Welcome back, {username}!")
            # profile will be collected below because no profile fields exist for a new user
            profile_exists = False
        else:
            print("Something went wrong. Try again later.")

# If profile not stored for the authenticated user, collect it now.
if not profile_exists:
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

        semester = ""  # default if not in high school
        if highschool == "yes":
            semester = input( "What semester are you in? (e.g., 1st, 2nd, 3rd, etc.): ")
            # Grade average calculation for feedback on academic performance
            grade_stu = collect_grades()
            avg_grade = grade_stu["Grade"].mean() if not grade_stu.empty else 0.0
            print("Grade average: ", avg_grade)
            if avg_grade < 70: 
                print ("Student with bad grades, must present PAA") 
            elif avg_grade >= 70 and avg_grade <= 80: 
                print ("Regular student, can request Alianza azul scholarship presenting PAA")
            elif avg_grade > 80 and avg_grade <= 90:
                print ("Student with good grades, can request Alianza azul scholarship presenting PAA")
            elif avg_grade > 90 and avg_grade <= 100:
                print ("Excelent student, can request Excelencia academica and Alianza azul scholarships")

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
        interest_list = ["Business", "Health", "Creative Studies", "Built Environment", "Law, Economics and International Relations", "Innovation and Transformation", "Computing and Information Technologies", "Bioengineering and Chemical Processes", "Applied Sciences"]
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

        # --- Save profile fields to users.csv (update or append) ---
        try:
            # Ensure profile columns exist (already ensured above)
            interests_str = json.dumps(selected_interest, ensure_ascii=False)

            mask = users["username"] == username
            if mask.any():
                users.loc[mask, "name"] = name
                users.loc[mask, "birthday"] = birthday
                users.loc[mask, "location"] = location
                users.loc[mask, "highschool"] = highschool
                users.loc[mask, "semester"] = semester if highschool == "yes" else ""
                users.loc[mask, "interests"] = interests_str
            else:
                # If for some reason the username row doesn't exist, append a new one.
                new_row = {
                    "username": username,
                    "password": password,
                    "name": name,
                    "birthday": birthday,
                    "location": location,
                    "highschool": highschool,
                    "semester": semester if highschool == "yes" else "",
                    "interests": interests_str
                }
                users = pd.concat([users, pd.DataFrame([new_row])], ignore_index=True)

            users.to_csv(file_path, index=False)
            print("\033[1;32mProfile saved to 'users.csv'.\033[0m")
        except Exception as e:
            print("\033[1;31mFailed to save profile to 'users.csv':\033[0m", repr(e))
        # ---------------------------------------------------------

        # Option to redo profile
        print("\n\033[1;37mDo you want to make changes to your profile? (yes/no):\033[0m ")
        change_profile = input().strip().lower()
        if change_profile in ("yes", "y"):
            continue
        else:
            print("\n\033[1;33mProfile created successfully!\033[0m")
            break
