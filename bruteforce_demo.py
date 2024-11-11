import itertools
import string

def check_password(guess):
    actual_password = "abdc"
    return guess == actual_password

def brute_force_attack():
    characters = string.ascii_lowercase
    max_length = 4

    for length in range(1, max_length + 1):
        for guess in itertools.product(characters, repeat=length):
            guess = ''.join(guess)
            print(f"Trying password: {guess}")
            if check_password(guess):
                print(f"Password found: {guess}")
                return guess
    
    print("Password not found")

brute_force_attack()