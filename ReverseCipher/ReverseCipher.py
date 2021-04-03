#Reverse Cipher
message = input('Enter text to encrypt it\n if you don\'t enter text\n '+
                'default text = Three can keep a secrete if two are dead\n '+
                'will be used instead\n')
if message == '':
    message = 'Three can keep a secrete if two are dead'
outPut = ''
#identifying the end of the text message
#For the purpose of clearity have changed variable encrypted to i
i = len(message)-1
#begining of the reverse cipher using a while loop
while i >= 0:
    outPut = outPut + message[i]
    i = i - 1

print(outPut)
