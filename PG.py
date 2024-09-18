import random
import string

def generate_password(length=12):
    if length < 8:
        raise ValueError("Password length must be at least 8 characters.")

    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Ensure the password contains at least one of each required character type
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the rest of the password length with random choices
    all_characters = lowercase + uppercase + digits + symbols
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the password list to ensure randomness
    random.shuffle(password)

    return ''.join(password)

def validate_password(password):
    if len(password) < 8:
        return False
    if not any(c.isupper() for c in password):
        return False
    if not any(c.islower() for c in password):
        return False
    if not any(c.isdigit() for c in password):
        return False
    if not any(c in string.punctuation for c in password):
        return False
    return True

def main():
    try:
        user_password = input("Enter your password for validation: ")
        if len(user_password) < 8:
            print("Password length must be at least 8 characters.")
            return

        if validate_password(user_password):
            print("Your password is valid.")
        else:
            print("Your password is invalid. It must contain at least One Uppercase letter, One Lowercase letter, One Digit, One Symbol, and be at least 8 characters long.")
        
    except ValueError:
        print("Please enter a valid number for the password length.")

if __name__ == "__main__":
    main()
