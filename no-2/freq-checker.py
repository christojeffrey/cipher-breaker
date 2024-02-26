# read cipherText
from cipher import cipherText

# any-gram
gramNumberToCheck = [3,4]
gramFrequency = {}


for gramNumber in gramNumberToCheck:
    for letter in range(len(cipherText) - gramNumber + 1):
        gram = cipherText[letter:letter + gramNumber]
        if gram in gramFrequency:
            gramFrequency[gram]["frequency"] += 1
            gramFrequency[gram]["location"].append(letter)
        else:
            gramFrequency[gram] = {
                "frequency": 1,
                "location" : [letter]
            }

# separator
print("========================================")
# sort and print
sorted_gramFrequency = sorted(gramFrequency.items(), key=lambda x: x[1]["frequency"], reverse=True)



top_gram = 20
# print top gram
for k, v in sorted_gramFrequency[:top_gram]:
    print(f"{k}: {v['frequency']} - {v['location']}")

print("difference: ")

differenceFrequency = {}
# calculate the difference between the location
for k, v in sorted_gramFrequency[:top_gram]:
    difference = []
    for index in range(len(v["location"]) - 1):
        diff = v["location"][index + 1] - v["location"][index]
        difference.append(diff)
        if diff in differenceFrequency:
            differenceFrequency[diff] += 1
        else:
            differenceFrequency[diff] = 1

    print(f"{k}: {difference}")

print("difference frequency: ")
top_difference = 20
# print the difference frequency
# sort and print
sorted_differenceFrequency = sorted(differenceFrequency.items(), key=lambda x: x[1], reverse=True)
for k, v in sorted_differenceFrequency[:top_difference]:
    print(f"{k}: {v}")


# find the biggest common factor
factors = {}
for k, v in sorted_differenceFrequency[:top_difference]:
    factors[k] = []
    for i in range(2, k):
        if k % i == 0:
            factors[k].append(i)
            

print("factors: ")
for k, v in factors.items():
    print(f"{k}: {v}")