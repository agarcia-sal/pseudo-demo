# Step 1: Get user input
print("Enter the first string:")
string1 = input()

print("Enter the second string:")
string2 = input()

# Step 2: Clean the input strings by removing spaces
cleanString1 = string1.replace(" ", "")
cleanString2 = string2.replace(" ", "")

# Step 3: Initialize a dictionary to hold frequency differences
frequencyDifferences = {}

# Step 4: Calculate the frequency of each character
for character in range(ord('A'), ord('z') + 1):  # loop from 'A' to 'z'
    char = chr(character)  # convert the ASCII value back to a character
    countInString1 = cleanString1.count(char)
    countInString2 = cleanString2.count(char)
    frequencyDifferences[char] = countInString1 - countInString2

# Step 5: Check if all frequency differences are non-negative
negativeFrequencyCount = 0

for difference in frequencyDifferences.values():
    if difference < 0:
        negativeFrequencyCount += 1

# Step 6: Output the result based on frequency check
if negativeFrequencyCount == 0:
    print("YES")
else:
    print("NO")
