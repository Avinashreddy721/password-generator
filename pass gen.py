import random
import string

def generate_password(length):
    # Define character sets for password generation
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all character sets
    all_characters = lower_case + upper_case + digits + special_characters

    # Generate password
    password = ''.join(random.sample(all_characters, length))
    return password

def main():
    try:
        # Prompt user to enter password length
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            print("Password length should be a positive integer.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid integer for password length.")
        return

    # Generate password
    password = generate_password(length)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
