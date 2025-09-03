# Created By: Matheus Ribeiro
# Name: César Cipher v1.0
# Launch: 9/2/2025 - 10:58 AM
# Latest: 9/2/2025 - 10:58 AM
# Description: A program for encryption, decryption and brake with César Cipher

import string

text = input('Text: ').lower()                # plaintext or ciphertext in lowercase for easily compare
mode = input('Mode (enc/dec/break): ')  
if mode != 'break':
    key = int(input('Key(1-26): '))  
lc = string.ascii_lowercase                   # Alphabet in lowercase
result = ''

 
if mode == 'break': 
    key = 1
    for count in range(0,26):
        for ch in text:
            if ch in lc:
                index = lc.find(ch)
                index = (index - key) % 26
                result += lc[index]           # Returns the encrypted characther
            else:
                result += ch                  # Only concatenates
        print(f'Key: {key:02} - * {result} *')
        key += 1
        result = ''     
else: 
    for ch in text:
        if ch in lc:
            index = lc.find(ch)               # Character position in lowercase alphabet
            if mode == 'enc':
                index = (index + key) % 26    # Dislocation to right
            elif mode == 'dec':
                index = (index - key) % 26    # Dislocation to left
            else:    
                print('***mode error***')
                break
            result += lc[index]               
        else:
            result += ch                      

    print(result, end='')