import random
import string

def main():
    while True:
        decision = input("do you want to generate password: (y/n)?")
        if decision == 'n':
            break 
        while True:
            length = int(input("Enter the desired password length: "))
            if length < 5:
                print("Password should be at least 5 characters long for security purposes.")
                continue
            break
        all_char = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(all_char) for _ in range(length))
        print("Generated password:", password)

if __name__ == "__main__":
    main()
