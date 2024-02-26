# used to help see the guessed result from uncomplete key. by making the pre deciphered text into a uppercase, and spliting text into the key length which is 12

from res1 import tempText

# split 12 characters into a list
splitted = []
for i in range(0, len(tempText), 12):
    splitted.append(tempText[i:i+12])
# make the first character uppercase
indexToUpper = [1, 2, 3, 4]
for twelveCharIndex in range(len(splitted)):
    temp = list(splitted[twelveCharIndex])
    for i in range(len(temp)):
        if i in indexToUpper:
            temp[i] = temp[i].upper()
        else:
            temp[i] = temp[i].lower()
    splitted[twelveCharIndex] = "".join(temp)

    
# join the list into a string with spaces
result = " ".join(splitted)

print(result)