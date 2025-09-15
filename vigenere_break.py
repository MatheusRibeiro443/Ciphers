# Created By: Matheus Ribeiro
# Name: Vigenere Break v1.0
# Launch: 9/15/2025 - 12:55 PM
# Latest: 9/15/2025 - 12:55 PM
# Description: A program for Vigènere Cipher break

import string 
from decimal import Decimal, getcontext 
getcontext().prec = 5 

portfreq = {                                                                            # Frequency of letters in the Portuguese alphabet
    'a': Decimal('0.1396'),
    'b': Decimal('0.0100'),
    'c': Decimal('0.0401'),
    'd': Decimal('0.0497'),
    'e': Decimal('0.1205'),
    'f': Decimal('0.0100'),
    'g': Decimal('0.0120'),
    'h': Decimal('0.0080'),
    'i': Decimal('0.0584'),
    'j': Decimal('0.0040'),
    'k': Decimal('0.0010'),
    'l': Decimal('0.0305'),
    'm': Decimal('0.0462'),
    'n': Decimal('0.0483'),
    'o': Decimal('0.1073'),
    'p': Decimal('0.0251'),
    'q': Decimal('0.0090'),
    'r': Decimal('0.0707'),
    's': Decimal('0.0778'),
    't': Decimal('0.0442'),
    'u': Decimal('0.0460'),
    'v': Decimal('0.0130'),
    'w': Decimal('0.0005'),
    'x': Decimal('0.0030'),
    'y': Decimal('0.0005'),
    'z': Decimal('0.0040')
} 

print('>'*10 + ' Welcome to Vigenère Break v1.0! ' + '<'*10) 

text = input('Text: ').lower() 
key_length = int(input('Min. Range Key: ')) 
key_size = int(input('Max. Range Key: ')) 
lc = string.ascii_lowercase 
letters_count = {} 
clean_text = '' 

if text == '' or key_length <= 0 or key_size < key_length: 
    print('***Incorrect Value Detected***') 
    raise SystemExit 

def ltc_def():                                                                         # Initialization of dict to all alphabet letters
    for define in lc: 
        letters_count[define] = 0 

for ch in text:                                                                        # Clear the text
    if ch in lc: 
        clean_text += ch 

while key_length <= key_size: 
    letters = [] 
    count = 0 
    while count < key_length: 
        letters.append(clean_text[count::key_length])                                  # Select the equivalent columns to one letter of key
        count+=1 
    count = 0  
    key = '' 
    while count < key_length: 
        lsum = Decimal(str(len(letters[count])))                                       # Store the length of character column for percentage calculation
        chi_square = {} 
        value = Decimal('Infinity') 
        current = 0

        for k in range(0,26):                                                          
            chi_square[k] = Decimal('0')                                                # Initialization the accumulator of chi-square
            ltc_def() 
            column = '' 

            for c in letters[count]:                                                    # Apply the left shift
                idx = lc.find(c) 
                idx -= k 
                column += lc[idx%26] 

            for lt in column:                                                           # Count the frequency of letters
                letters_count[lt]+=1 

            for ltc in sorted(letters_count, key=letters_count.get, reverse=True): 
                chi_square[k] += ((letters_count[ltc] - portfreq[ltc])**2)/portfreq[ltc] # Calculate chi-square

        for read in chi_square:                                                          # Store the smallest chi-square and your key
            if value > chi_square[read]: 
                value = chi_square[read] 
                current = read 
                
        key+=lc[current]                                                                 
        count+=1 
    print(f'{key_length} - {key}') 
    key_length+=1 
print('='*25 + ' END ' + '='*25) 