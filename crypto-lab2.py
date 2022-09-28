from random import sample
from itertools import product as col


def generator(key,letter,length):
    char_len = key.count(letter)   
    key_piece = key[:length - char_len:]
    list_keys = [key_piece+"".join(i) for i in list(col([chr(i) for i in range(65, 65+26)], repeat=char_len))]
    return list_keys
	
def vigenere(plainTxt,key):
    modifiedTxt = []
    wordArray = list(plainTxt)
    #The list () function creates a list object. A list object is a collection which is ordered and changeable
    j = 0
	
    for i,letter in enumerate(wordArray):
        #wordArray = ('apple', 'banana', 'cherry')
        #y = enumerate(plainTxt) => [(0,apple),(1,banana),(2,cherry)]
        if letter.isalpha():
            wordArray[i] = key[(i+j)%len(key)]
            if encrypt:
                #ord function gives unicode of aplphabet ord(h) =>104
                modifiedTxt.append((ord(plainTxt[i]) + ord(wordArray[i]) - 65 * 2) % 26)
            else:
                modifiedTxt.append((ord(plainTxt[i]) - ord(wordArray[i])) % 26)
        else:
            modifiedTxt.append(ord(letter))
            j -=1

    for i,letter in enumerate(wordArray):
        if letter.isalpha():
            modifiedTxt[i] = chr(modifiedTxt[i] + 65)
        else:
            modifiedTxt[i] = chr(modifiedTxt[i])
			
    return ''.join(modifiedTxt)

print("\n********** Vigenere Cipher **********")
a = input('\nDo you want to Encrypt or Decrypt? : ')
if a.lower() == 'encrypt':
    plainTxt = input('Enter the text : ').upper()
    key = input('\nEnter the key : ').upper()
    encrypt = True
    print('\nThe encrypted text is : \n')
    print(vigenere(plainTxt,key))
else:
    plainTxt = input('text : ').upper()
    encrypt = False
    key = input('\nEnter the key : ').upper()
    print('\nThe decrypted text is : \n')
    print(vigenere(plainTxt,key))
   