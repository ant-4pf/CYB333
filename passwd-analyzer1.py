print("Password Strength Analyzer")


password = input("Enter your password: ")
length = len(password)
SC = "!@#$%^&*()-_=+[]}{/?<>|:\;\`~"
strength_score = 0


def calculate_strength(password):
    global strength_score
    if any(char.islower() for char in password):
        strength_score += 1
    if any(char.isupper() for char in password):
        strength_score += 1
    if any(char.isdigit() for char in password):
        strength_score += 2
    if any(char in SC for char in password):
        strength_score += 2
    if length < 8:
        print("Password should be at least 8 characters long.")
    elif length >= 8 and length < 12:
        strength_score += 1
        print("Password is good, but could be stronger.")
    elif length >= 12 and length >= 16:
        strength_score += 3
        print("Password is strong!")
    else:
        strength_score += 2
        print("Password is VERY strong!")

print("Analyzing password strength. . .")
calculate_strength(password)
print(f"Password Strength Score: {strength_score}") 