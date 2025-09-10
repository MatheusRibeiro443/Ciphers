# Created By: Matheus Ribeiro
# Name: Vernam Cipher v1.0
# Launch: 9/10/2025 - 6:04 PM
# Latest: 9/10/2025 - 6:04 PM
# Description: A program for encryption and decryption with Vernam Cipher

import binascii                                             # Binary Operations

print('>'*10 + ' Welcome to Vernam Cipher v1.0! ' + '<'*10)
text = input('Text: ')
key = input('Key: ')
action = input('Action (enc/dec): ')
keyidx = 0
newtext = ['']

if action == 'dec':
    text = binascii.unhexlify(text).decode()                 # Hex to Byte + Byte to Ascii

for ch in text:
    newtext.append(chr(ord(ch) ^ ord(key[keyidx%len(key)]))) # XOR Operation + Ascii to Dec + Dec to Ascii
    keyidx+=1

newtext = ''.join(newtext)

if action == 'dec':
    print(f'{newtext}')
elif action == 'enc':
    print(f'{binascii.hexlify(newtext.encode())}')           # Ascii to Byte + Byte to Hex