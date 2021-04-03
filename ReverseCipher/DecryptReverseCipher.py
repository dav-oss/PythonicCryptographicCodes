#to decrypt the message the code is the same the only thing that changes is the input
#take a look of the code below
encrypted = input('Enter your text below to dencrypt it\n if you don\'t enter a text it '+
                  'will use the default:\n text = daed era owt fi eterces a peek nac eerhT\n')
if encrypted == '':
    encrypted = 'daed era owt fi eterces a peek nac eerhT'

decrypted = ''
#first we have to identify the end of the string
i = len(encrypted) - 1
#decryption starts here

while i >= 0:
    decrypted = decrypted + encrypted[i]
    i = i - 1

print(decrypted)
