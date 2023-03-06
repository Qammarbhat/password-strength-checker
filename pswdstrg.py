import re

def password_strength(password):
    score = 0

    # Check password length
    if len(password) >= 8:
        score += 1

    # Check for uppercase letters
    if re.search('[A-Z]', password):
        score += 1

    # Check for lowercase letters
    if re.search('[a-z]', password):
        score += 1

    # Check for digits
    if re.search('[0-9]', password):
        score += 1

    # Check for symbols
    if re.search('[^a-zA-Z0-9]', password):
        score += 1

    # Return password strength score
    return score

# Prompt user for password input
password = input("Enter a password to check its strength: ")

# Assess password strength and display result
strength_score = password_strength(password)
if strength_score == 0:
    print("Password is weak")
elif strength_score <= 2:
    print("Password is moderate")
else:
    print("Password is strong")