# used to break vigenere, given the size of the key

from cipher import cipherText

keySize = 12

# letterIndexToCheck = 7

letterFrequency = {}

filteredText = "" # only consist of the letterIndexToCheck, after divided by keySize. let's say 12 is the key size, and the index is 0. then it's letter 0, 12, 24, 36, etc 
for letterIndexToCheck in range(keySize):
    localFrequency = {}
    for i in range(len(cipherText)):
        if i % keySize == letterIndexToCheck:
            filteredText += cipherText[i]
            key = str(letterIndexToCheck + 1) + " " + cipherText[i]
            if key in letterFrequency:
                letterFrequency[key] += 1
            else:
                letterFrequency[key] = 1

            # add to local frequency
            if cipherText[i] in localFrequency:
                localFrequency[cipherText[i]] += 1
            else:
                localFrequency[cipherText[i]] = 1
    # print the most frequent letter in local frequency
    sorted_localFrequency = sorted(localFrequency.items(), key=lambda x: x[1], reverse=True)
    print(f"letter index: {letterIndexToCheck + 1}")
    for k, v in sorted_localFrequency[:10]:
        print(f"{k}: {v}")



print("========================================")

# # print beautifully
# sorted_letterFrequency = sorted(letterFrequency.items(), key=lambda x: x[1], reverse=True)
# for k, v in sorted_letterFrequency[:10]:
#     print(f"{k}: {v}")