intro_text = """Welcome to BUILD YOUR OWN PATH!
Let's start by creating your profile."""

# Add a blank line between each line
spaced_intro_text = "\n\n".join(intro_text.splitlines())

print(spaced_intro_text)

# Building user profile
name = input("Enter your name: ")
birthday = input("Enter your birthday (DD-MM-YYYY): ")
location = input("Enter your location: ")
highschool = input( "Are you in high school? (yes/no): ").strip().lower()
if highschool in ("yes", "y"):
    highschool = "yes"
else:
    highschool = "no"

if highschool == "yes":
    semester = input( "What semester are you in? (e.g., 1st, 2nd, 3rd, etc.): ")

# Area of interest selection
interest_list = ["Ambiente Construido", "Negocios", "Derecho, Economia y Relaciones Internacionales", "Estudios Creativos", "Salud", "Ingenieria"]
print("\nSelect your area of interest from the list below (separate multiple choices with commas): ")
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
print("\nUser Profile:")
print(f"Name: {name}")
print(f"Birthday: {birthday}")
print(f"Location: {location}")
print(f"In High School: {highschool}")
if highschool == "yes":
    print(f"Semester: {semester}")
print(f"Areas of Interest: {', '.join(selected_interest) if selected_interest else 'None'}")
