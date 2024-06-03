import string
import random
import pickle

def get_password_length():
    try:
        length = int(input("Enter the desired length of the password (minimum 8): "))
        if length < 8:
            print("Password length should be at least 8 characters for better security.")
            return get_password_length()
        return length
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return get_password_length()

def get_password_complexity():
    print("Choose the complexity of the password:")
    print("1. Only letters")
    print("2. Letters and digits")
    print("3. Letters, digits, and special characters")
    
    choice = input("Enter your choice (1/2/3): ")
    if choice in ['1', '2', '3']:
        return int(choice)
    else:
        print("Invalid choice. Please choose from 1, 2, or 3.")
        return get_password_complexity()

def generate_password(length, complexity):
    characters = string.ascii_letters
    if complexity > 1:
        characters += string.digits
    if complexity > 2:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def save_password(password):
    with open('password.pkl', 'wb') as file:
        pickle.dump(password, file)

def load_password():
    try:
        with open('password.pkl', 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return "No previous password found."

def main():
    length = get_password_length()
    complexity = get_password_complexity()
    password = generate_password(length, complexity)
    print(f"Generated password: {password}")
    save_password(password)
    
    previous_password = load_password()
    print(f"Previous password: {previous_password}")

if __name__ == "__main__":
    main()
