import random
import string

def generate_password(length):
    # Define characters to choose from
    chars = string.ascii_letters + string.digits + string.punctuation
    # Generate password using random.choices for secure random selection
    password = ''.join(random.choices(chars, k=length))
    return password

def main():
    print("\nWelcome to the Secure Password Generator!")
    print("=========================================")
    while True:
        try:
            # Get user input for password length
            length = int(input("Enter the length of the password you want to generate (8-32 characters recommended): "))
            if length < 8:
                print("Password length too short. Minimum recommended length is 8 characters.")
                continue
            if length > 32:
                print("Password length too long. Maximum recommended length is 32 characters.")
                continue
            # Get user input for number of passwords
            num_passwords = int(input("Enter the number of passwords you want to generate: "))
            if num_passwords <= 0:
                print("Please enter a valid number of passwords (greater than 0).")
                continue
            # Generate specified number of passwords
            print("\nGenerating {} passwords...".format(num_passwords))
            for i in range(num_passwords):
                password = generate_password(length)
                print("Password {}: {}".format(i+1, password))
            break
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
