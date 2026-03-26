
print("        PASSWORD STRENGTH CHECKER")


password = input("Enter your password: ")

score = 0

if len(password) >= 8:
    score += 1


if any(c.isupper() for c in password):
    score += 1


if any(c.islower() for c in password):
    score += 1


if any(c.isdigit() for c in password):
    score += 1

if any(c in "!@#$%^&*()_+-=" for c in password):
    score += 1

print("\nChecking password strength...")



if score <= 2:
    print("Password Strength : WEAK")
    print("Suggestion: Use uppercase, numbers, and special characters.")
elif score == 3 or score == 4:
    print("Password Strength : MEDIUM")
    print("Suggestion: Add more variety to make it strong.")
else:
    print("Password Strength : STRONG")
    print("Great! Your password is secure.")

