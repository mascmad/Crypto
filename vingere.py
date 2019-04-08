#! /usr/bin/python3
# Allows a user to encrypt, decrypt, or brute force a vingere cipher.
import sys  

alphabet = 'abcdefghijklmnopqrstuvwxyz'
msg = sys.argv
msg.pop(0)  # remove the first argument; the path to the file

# msg[0] = file path
message = msg[1]
key = msg[2]

msg_nums = []
key_nums = []

def help_func(invalid=False):
    if invalid:
        print("ERROR: Invalid option. Usage:")
    # TODO: make this legit using option parser
    print("vingere.py\n\t[-e \"message\" \"key\"]\n\t[-d \"message\" \"key\"]\n\t[-b \"message\" path-to-wordlist]")


# TODO: help menu, argument verification, and all that stuff

# TODO: captials

def encrypt(message_str, key_str):
    # turn each character in message into a number
    for i in range(0, len(message_str)):
        # ascii codes:
        # a = 97, z = 122
        msg_nums.append(ord(message_str[i]))
    print("pre-msg_nums:", msg_nums)
    # and do the same for the key
    for i in range(0, len(key_str)):
        key_nums.append(ord(key_str[i]))
    print("key_nums:", key_nums)
    #
    print("len msg_nums:", len(msg_nums), "| len key_nums:", len(key_nums))
    for i in range(0, len(msg_nums)):
        for j in range(0, len(key_nums)):
            # do stuff
            print("i in j:", i, end=', ')
            print("pre:", msg_nums[i], end=', ')
            msg_nums[i] += (key_nums[j] - ord('a') + 1)
            print("msg_nums[i]:", msg_nums[i], end=', ')
            print("chr():", chr(msg_nums[i]))
            if j == len(msg_nums) - 1:
                print("i >= keynums")
                break
    print("post-msg_nums:", msg_nums)
    # revert to letters
    for i in range(0, len(msg_nums)):
        print(chr(msg_nums[i]), end='')



if msg[0] == "-e":
    encrypt(message, key)
elif msg[0] == "-d":
    print("Decryption function not yet available.")
elif msg[0] == "-b":
    print("Brute force function not yet available.")
else:
    help_func(1)

