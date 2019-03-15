#! /usr/bin/python3
# brute forces a rot-x cipher through all 26 letters of the alphabet
import sys

message = ''
alphabet = 'abcdefghijklmnopqrstuvwxyz'
msg = sys.argv
msg.pop(0)
message = str(msg)

# array for positions of capital characters in the message
caps = []

# loop through the entire message to find what characters are capitals
for l in range(0, len(message)):
    if message[l].isupper():
        caps.append(l)

# Make the input lowercase to make it easer to work with
message = message.lower()

# begin looping through all the alphabet (x is the key)
for x in range(1, 26):
    str_out = ''
    print(str(x) + ':\t', end='')

    # begin looping through the message
    for i in range(0, len(message)):
        # error-checking
        try:
            # index of the shifted letter
            f = alphabet.index(message[i]) + x
            if 0 > f:       # if the number would go under the length of the array
                a = f + 26
                str_out += alphabet[a]
            elif 26 <= f:   # if the number would go above the length of the array
                b = f - 26
                str_out += alphabet[b]
            else:
                str_out += alphabet[f]
        except ValueError:  # if the character is a number or otherwise non-alphanumeric
            str_out += message[i]
    for n in caps:
        str_out = str_out.replace(str_out[n], str_out[n].capitalize())
    str_out = str_out.replace("[", "").replace("'", "").replace(",", "").replace("]", "")
    print(str_out)
