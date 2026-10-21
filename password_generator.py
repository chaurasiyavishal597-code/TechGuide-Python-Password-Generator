
import string
import secrets
import random


def generate_password(length):
    if length < 8:
        raise ValueError("Password length must be at least 8.")

    # Character categories
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    symbols = "!@#$%^&*()-_=+?"

    # Ensure at least one character from each category
    password_chars = [
        secrets.choice(uppercase),
        secrets.choice(lowercase),
        secrets.choice(digits),
        secrets.choice(symbols)
    ]

    # Combine all allowed characters
    all_characters = uppercase + lowercase + digits + symbols

    # Fill the remaining length
    for _ in range(length - 4):
        password_chars.append(secrets.choice(all_characters))

    # Securely shuffle the characters
    secrets.SystemRandom().shuffle(password_chars)

    return "".join(password_chars)


def main():
    print("\n===== PASSWORD GENERATOR =====")

    try:
        length = int(input("Enter password length (minimum 8): "))

        if length < 8:
            print("Error: Password length must be at least 8.")
            return

        count = int(input("How many passwords do you want? "))

        if count < 1 or count > 10:
            print("Enter a count between 1 and 10.")
            return

        print("\nGenerated Passwords:")

        for number in range(1, count + 1):
            password = generate_password(length)
            print(f"{number}. {password}")

        print("\nPassword generation completed!")

    except ValueError as error:
        print("Invalid input:", error)


if __name__ == "__main__":
    main()
