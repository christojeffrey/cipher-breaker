# read cipherText
from cipher import cipherText
# replace E with E - good
plainTextGuess = cipherText.replace("E", "e")

# replace H with T - good
plainTextGuess = plainTextGuess.replace("H", "t")

# A - S
plainTextGuess = plainTextGuess.replace("A", "s")

# L - I
plainTextGuess = plainTextGuess.replace("L", "i")
# Y - A
plainTextGuess = plainTextGuess.replace("Y", "a")

# replace R with O 
plainTextGuess = plainTextGuess.replace("R", "o")

# B - R
plainTextGuess = plainTextGuess.replace("B", "r")

# F - N
plainTextGuess = plainTextGuess.replace("F", "n")

# Z -> H
plainTextGuess = plainTextGuess.replace("Z", "h")

# T - W
plainTextGuess = plainTextGuess.replace("T", "w")

# P - M
plainTextGuess = plainTextGuess.replace("P", "m")

# O - G
plainTextGuess = plainTextGuess.replace("O", "g")

# T - W
plainTextGuess = plainTextGuess.replace("T", "w")

# G - F
plainTextGuess = plainTextGuess.replace("G", "f")

# X - C
plainTextGuess = plainTextGuess.replace("X", "c")

# V - P
plainTextGuess = plainTextGuess.replace("V", "p")

# U - U
plainTextGuess = plainTextGuess.replace("U", "u")

# M - Y
plainTextGuess = plainTextGuess.replace("M", "y")

# W - L
plainTextGuess = plainTextGuess.replace("W", "l")

# C - D
plainTextGuess = plainTextGuess.replace("C", "d")

# K - B
plainTextGuess = plainTextGuess.replace("K", "b")

# I - K
plainTextGuess = plainTextGuess.replace("I", "k")

# D - X
plainTextGuess = plainTextGuess.replace("D", "x")

# N - V
plainTextGuess = plainTextGuess.replace("N", "v")

# Q - Q
plainTextGuess = plainTextGuess.replace("Q", "q")

# S - Z
plainTextGuess = plainTextGuess.replace("S", "z")

# J - J
plainTextGuess = plainTextGuess.replace("J", "j")


print(plainTextGuess)
# save to temp.txt
with open("temp.txt", "w") as file:
    file.write(plainTextGuess)


# replace A with A


# replace L1 with L2
# replace L3 with L4

# note to self, L2 shouldn't never be the same with L3. this will replace the letter two times. 