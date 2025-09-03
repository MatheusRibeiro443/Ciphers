# Created By: Matheus Ribeiro
# Name: Vigenère Cipher v1.0
# Launch: 9/3/2025 - 10:15 AM
# Latest: 9/3/2025 -  6:08 PM
# Description: A program for encryption, decryption with Vigenère Cipher

import string

print('>'*10 + ' Welcome to Vigenére Cipher v1.0! ' + '<'*10)
text = input('Text: ').lower()
key = input('Key: ')
action = input('Action (enc/dec): ')
lower = string.ascii_lowercase
result = ''
keyidx = 0                                               # index for runs through of key

for ch in text:
    if ch in lower:
        idx = lower.find(ch)
        if action == 'enc':
            idx = idx + lower.find(key[keyidx%len(key)]) # Runs throug the key, limiting keyidx by key length using mod
        elif action == 'dec':
            idx = idx - lower.find(key[keyidx%len(key)]) # After, obtain the equivalent value in lowercase alphabet and combine with current characther
        else:
            print('***Invalid Action***')
        result += lower[idx % 26]                        # Applied the mod operation in index, for maintaining in range of alphabet
        keyidx += 1
    else:
        result += ch

print(f'{result}')