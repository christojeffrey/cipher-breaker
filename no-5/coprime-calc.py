# find the coprime numbers of a given number

import math

number = 256

coprime_numbers = [i for i in range(1, number) if math.gcd(i, number) == 1]

print(coprime_numbers)
