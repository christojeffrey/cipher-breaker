# find the key from given cipher and plain text for vigenere

cipherText = "PZSE"
plainText = "IVER"

key = ""
for i in range(len(cipherText)):
    key += chr((ord(cipherText[i]) - ord(plainText[i])) % 26 + 65)

print(key)