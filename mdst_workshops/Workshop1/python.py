"""
MDST Workshop 1 - Python Basics Starter Code
"""

# Add any imports you need here:
import cryptography
from cryptography.fernet import Fernet


def part1(num):
    """
    Ask the user for a number. Depending on whether the number is even or odd,
    print out an appropriate (i.e. "even" or "odd") message to the user.
    """

    num = int(input("Enter a number: "))
    if (num % 2 == 0) :
        print("Even")
    else:
        print("Odd")

def part2():
    """
    Generate a random number between 1 and 9 (including 1 and 9). Ask the user
    to guess the number, then tell them whether they guessed too low, too high,
    or exactly right.
    (Hint: remember to use the user input lessons from the very first
    exercise).
    Keep the game going until the user types "exit".
    [ try checking the random module in python on google. Concepts: Infinite
    loops, if, else, loops and user/input].
    """
    import random
    number = random(1,9)
    guess = 0

    while guess != number and guess != "exit":
        guess = input("What's your guess?")

        if guess == "exit":
            break
        guess = int(guess)

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print("You got it!")

def part3(string):
    """
    Ask the user for a string and print out whether this string is a palindrome
    or not. (A palindrome is a string that reads the same forwards and
    backwards.)
    """

    word = input("Please enter a word")
    word = str(word)
    reverse = word[::-1]
    print(reverse)
    if word == reverse:
        print("This word is a palindrome")
    else:
        print("This word is not a palindrome")

def part4a(filename, username, password):
    """
    Encrypt your username and password using base64 module
    Store your encrypted username on the first line and your encrypted password
    on the second line.
    """

    key = Fernet.generate_key()
    file = open(filename, "w")
    file.write(key)
    file.close()

    user_encoded = username.encoded()
    f = Fernet(key)
    user_encyrpted = f.encrypt(user_encoded)
    file = open(file, 'w')
    file.write(user_encyrpted)

    pass_encoded = password.encoded()
    f = Fernet(key)
    pass_encyrpted = f.encrypt(pass_encoded)
    file = open(filename, 'w')
    file.write(pass_encyrpted)


def part4b(filename, password=None):
    """
    Create a function to read the file with your login information.
    Print out the decrypted username and password.
    If a password is specified, update the file with the new password.
    """
    f = open(filename, "r")
    key = f.read()
    user_en = f.read()
    pass_en = f.read()
    f2 = Fernet(key)
    org_username = f2.decrypt(user_en)
    org_password = f2.decrypt(pass_en)
    print(org_username)
    print(org_password)

if __name__ == "__main__":
    part1(3)  # odd!
    part1(4)  # even!
    part2()
    part3("ratrace")  # False
    part3("racecar")  # True
    part4a("secret.txt", "naitian", "p4ssw0rd")
    part4b("secret.txt")
    part4b("secret.txt", password="p4ssw0rd!")
    part4b("secret.txt")
