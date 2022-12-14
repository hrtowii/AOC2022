# lowercaseAlphabet = "abcdefghijklmnopqrstuvwxyz"
# uppercaseAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# lowercaseNumbers = list(range(1, 27))
# uppercaseNumbers = list(range(27, 53))

# lowercaseDict = dict(zip(lowercaseAlphabet, lowercaseNumbers))
# uppercaseDict = dict(zip(uppercaseAlphabet, uppercaseNumbers)) 

# totalSum = 0

# def removenewLine():
#     for i, line in enumerate(lines):
#         lines[i] = line.strip() # remove \n


# with open("day3input.txt",'r') as readfile:
#     lines = readfile.readlines()
#     removenewLine()
#     for line in lines:
#         compartment1 = line[:len(line) // 2]
#         compartment2 = line[len(line) // 2:] # courtesy of openAI lmao
#         # Use sets to find the common characters in both compartments
#         common_chars = set(compartment1).intersection(set(compartment2))
#         x = ''.join(common_chars)
#         for char in len(x):
#             if char.isupper():
#                 totalSum += uppercaseDict.get(char) # important, to be reused
#             else:
#                 totalSum += lowercaseDict.get(char)

# print(totalSum)
# #part 2
# count = 0
# totalSum = 0
# with open("day3input.txt", 'r') as readfile:
#     lines = readfile.readlines()
#     removenewLine()
# # Loop through the list in groups of three lines
# for i in range(0, len(lines), 3): # courtesy of openAI, how does this work???
#     # Create a set for each group of three lines
#     set1 = set(lines[i])
#     set2 = set(lines[i+1])
#     set3 = set(lines[i+2])
    
#     # Check if any two of the sets have at least one character in common
#     if set1 & set2:
#         x = ''.join(set1.intersection(set2))
#         for char in len(x):
#             if char.isupper():
#                 totalSum += uppercaseDict.get(char) # important, to be reused
#             else:
#                 totalSum += lowercaseDict.get(char)
#     elif set1 & set3:
#         x = ''.join(set1.intersection(set3))
#         for char in len(x):
#             if char.isupper():
#                 totalSum += uppercaseDict.get(char) # important, to be reused
#             else:
#                 totalSum += lowercaseDict.get(char)
#     elif set2 & set3:
#         x = ''.join(set2.intersection(set3))
#         for char in len(x):
#             if char.isupper():
#                 totalSum += uppercaseDict.get(char) # important, to be reused
#             else:
#                 totalSum += lowercaseDict.get(char)
#     else:
#         print("None of these lines have a character in common.")

# print(totalSum)
lowercaseAlphabet = "abcdefghijklmnopqrstuvwxyz"
uppercaseAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercaseNumbers = list(range(1, 27))
uppercaseNumbers = list(range(27, 53))

lowercaseDict = dict(zip(lowercaseAlphabet, lowercaseNumbers))
uppercaseDict = dict(zip(uppercaseAlphabet, uppercaseNumbers)) 

totalSum = 0

def removenewLine():
    for i, line in enumerate(lines):
        lines[i] = line.strip() # remove \n

with open("day3input.txt",'r') as readfile:
    lines = readfile.readlines()
    removenewLine()
    for line in lines:
        compartment1 = line[:len(line) // 2]
        compartment2 = line[len(line) // 2:]
        # Use sets to find the common characters in both compartments
        common_chars = set(compartment1).intersection(set(compartment2))
        x = ''.join(common_chars)
        for char in x:
            if char.isupper():
                totalSum += uppercaseDict.get(char)
            else:
                totalSum += lowercaseDict.get(char)

print(totalSum)

#part 2, doesn't work!!!
count = 0
totalSum = 0
with open("day3input.txt", 'r') as readfile:
    lines = readfile.readlines()
    removenewLine()

# Loop through the list in groups of three lines
for i in range(0, len(lines), 3):
    # Create a set for each group of three lines
    set1 = set(lines[i])
    set2 = set(lines[i+1])
    set3 = set(lines[i+2])
    
    # Check if any two of the sets have at least one character in common
    if set1 & set2:
        x = ''.join(set1.intersection(set2))
        for char in x:
            if char.isupper():
                totalSum += uppercaseDict.get(char)
            else:
                totalSum += lowercaseDict.get(char)
    elif set1 & set3:
        x = ''.join(set1.intersection(set3))
        for char in x:
            if char.isupper():
                totalSum += uppercaseDict.get(char)
            else:
                totalSum += lowercaseDict.get(char)
    elif set2 & set3:
        x = ''.join(set2.intersection(set3))
        for char in x:
            if char.isupper():
                totalSum += uppercaseDict.get(char)
            else:
                totalSum += lowercaseDict.get(char)
    elif set1 & set2 & set3:
        x = ''.join(set2.intersection(set3))
        for char in x:
            if char.isupper():
                totalSum += uppercaseDict.get(char)
            else:
                totalSum += lowercaseDict.get(char)
        print("None of these lines have a character in common.")

print(totalSum)
