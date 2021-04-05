#Ceaser Cipher Bruteforce program
message = 'guv6Jv6Jz!J6rp5r7Jzr66ntrM'
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

#Looping through every possible key
for key in range(len(SYMBOLS)):
    translated = ''
    
#Looping through each symbol in message
    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex - key

            #Handle the wraparound
            if translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)
            #Append the decrypted symbol
            translated = translated + SYMBOLS[translatedIndex]
        else:
            #appending the symbol without decrypting
            translated = translated + symbol
        #Since the message and the cipher text are of same length
        #We can evaluate the correct length of string/sentence to avoid
        #The big chunk of text appearing on the screen
        if len(message) == len(translated):
            print('Key #%s: %s' %(key, translated))
            #Now seems better to display the text to the user 
