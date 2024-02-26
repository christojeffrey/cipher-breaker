# read cipherText
from cipher import cipherText


# create dictionary of letter frequencies
letterFrequency = {}


# iterate through each letter, and add to letterFrequency

for letter in cipherText:
    if letter in letterFrequency:
        # if exist, increment
        letterFrequency[letter] += 1
    else:
        # if not exist, add to dictionary
        letterFrequency[letter] = 1

# sort based on letterFrequency
sorted_letterFrequency = sorted(letterFrequency.items(), key=lambda x: x[1], reverse=True)

# print beautifully
for k, v in sorted_letterFrequency:
    print(f"{k}: {v}")


bigramFrequency = {}
for letter in range(len(cipherText) - 1):
    bigram = cipherText[letter] + cipherText[letter + 1]
    if bigram in bigramFrequency:
        # 
        bigramFrequency[bigram] = bigramFrequency[bigram] + 1
    else:
        bigramFrequency[bigram] = 1


# separator 
print("========================================")
# sort and print
sorted_bigramFrequency = sorted(bigramFrequency.items(), key=lambda x: x[1], reverse=True)
for k, v in sorted_bigramFrequency[:20]:
    print(f"{k}: {v}")


# trigram
trigramFrequency = {}
for letter in range(len(cipherText) - 2):
    trigram = cipherText[letter] + cipherText[letter + 1] + cipherText[letter + 2]
    if trigram in trigramFrequency:
        trigramFrequency[trigram] = trigramFrequency[trigram] + 1
    else:
        trigramFrequency[trigram] = 1

# separator
print("========================================")
# sort and print
sorted_trigramFrequency = sorted(trigramFrequency.items(), key=lambda x: x[1], reverse=True)

# print top 5 trigram
for k, v in sorted_trigramFrequency[:10]:
    print(f"{k}: {v}")

# separator
print("========================================")
# quadgram
quadgramFrequency = {}
for letter in range(len(cipherText) - 3):
    quadgram = cipherText[letter] + cipherText[letter + 1] + cipherText[letter + 2] + cipherText[letter + 3]
    if quadgram in quadgramFrequency:
        quadgramFrequency[quadgram] = quadgramFrequency[quadgram] + 1
    else:
        quadgramFrequency[quadgram] = 1

# sort and print
sorted_quadgramFrequency = sorted(quadgramFrequency.items(), key=lambda x: x[1], reverse=True)

# print top 5 quadgram
for k, v in sorted_quadgramFrequency[:5]:
    print(f"{k}: {v}")
    