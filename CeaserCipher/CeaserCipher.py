#Cease Cipher


#The string to be encrypted
message = 'This is my secret message'

#setting the key to be used to encrypt the message
key = 13

#determing the mode by which the program will operate
mode = 'encrypt'#you can set it to decrypt if you wish to

#Every possible symbol that can be encrypted
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.`~@#$%^&*()_+-=[]{}|;:<>,/'

#Store the encrypted/decrypted form of the message
translated = ''

for symbol in message:
    #Note only symbol in the SYMBOLS string can be encrypted/decrypted
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)

        #Performing encryption/decryption
        if mode == 'encrypt':
            translatedIndex = symbolIndex + key
        elif mode == 'decrypt':
            translatedIndex = symbolIndex - key

        #Handling wraparound if needed:
        if translatedIndex >= len(SYMBOLS):
            translatedIndex = translatedIndex - len(SYMBOLS)
        elif translatedIndex < 0:
            translatedIndex = translatedIndex + len(SYMBOLS)
            
        translated = translated + SYMBOLS[translatedIndex]
    else:
        #appending the symbols without encrypting or decrypting
        translated = translated + symbol
    #Output the translated string
print(translated)
        
