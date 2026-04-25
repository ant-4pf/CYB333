print("Password Strength Analyzer")

import getpass

password = getpass.getpass("Enter your password: ")
length = len(password)
SC = "!@#$%^&*()|-_=+[]}{/?<>:"
strength_score = 0
max_length = 25

def calculate_strength(password, length):
    score = 0
    length = len(password)
    feedback = ""
    
    # Check character types
    has_lower = any(char.islower() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in SC for char in password)
    
    if has_lower:
        score += 1
    if has_upper:
        score += 1
    if has_digit:
        score += 2
    if has_special:
        score += 2
    
    # Length-based scoring and feedback
    if length > max_length:
        feedback = "Password is too long. Consider using a shorter password."
    elif length < 8:
        feedback = "Password should be at least 8 characters long."
    elif 8 <= length < 12:
        score += 1
        feedback = "Password is good, but could be stronger."
    elif 12 <= length < 16:
        score += 2
        feedback = "Password is strong!"
    else:  # length >= 16
        score += 3
        feedback = "Password is VERY strong!"
    return score, feedback

print("Analyzing password strength. . .")
strength_score, feedback = calculate_strength(password, length)
print(feedback)
print(f"Password Strength Score: {strength_score}") 