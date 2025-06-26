import re

# Common weak patterns to avoid
common_patterns = ['1234', 'password', 'qwerty', 'abcd', 'admin']

def evaluate_password(password):
    suggestions = []
    strength = ""
    
    # Criteria checks
    length_ok = len(password) >= 8
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'\d', password))
    has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    is_common = any(p in password.lower() for p in common_patterns)

    # Determine strength
    if all([length_ok, has_upper, has_lower, has_digit, has_special]) and not is_common:
        strength = "Strong paasword!"
    elif length_ok and ((has_upper and has_lower) or (has_digit and has_special)):
        strength = "Moderate password!"
        if not has_upper:
            suggestions.append("Add an uppercase letter.")
        if not has_lower:
            suggestions.append("Add a lowercase letter.")
        if not has_digit:
            suggestions.append("Include at least one number.")
        if not has_special:
            suggestions.append("Include a special character.")
    else:
        strength = "Weak password!"
        if not length_ok:
            suggestions.append("Make the password at least 8 characters long.")
        if not has_upper:
            suggestions.append("Add an uppercase letter.")
        if not has_lower:
            suggestions.append("Add a lowercase letter.")
        if not has_digit:
            suggestions.append("Include at least one number.")
        if not has_special:
            suggestions.append("Include a special character.")
        if is_common:
            suggestions.append("Avoid using common words or sequences.")

    return strength, suggestions

# CLI Main
if __name__ == "__main__":
    pwd = input("Enter your password: ")
    result, feedback = evaluate_password(pwd)

    print(f"\nPassword Strength: {result}")
    if feedback:
        print("Suggestions to improve:")
        for tip in feedback:
            print(f"- {tip}")
    else:
        print("Your password is secure!")
