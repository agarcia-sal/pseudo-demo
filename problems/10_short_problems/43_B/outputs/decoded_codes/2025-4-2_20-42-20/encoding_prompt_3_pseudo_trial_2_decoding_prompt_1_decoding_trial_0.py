# Step 1: Get user input
print("Enter the first string:")
string1 = input()

print("Enter the second string:")
string2 = input()

# Step 2: Clean the input strings by removing spaces
cleanString1 = string1.replace(" ", "")
cleanString2 = string2.replace(" ", "")

# Step 3: Initialize a list to hold frequency differences
# ASCII values for 'A' to 'z' is from 65 to 122 (inclusive)
frequencyDifferences = [0] * (123) # to cover ASCII 0-122

# Step 4: Calculate the frequency of each character
for character in range(65, 123):  # ASCII range for 'A' (65) to 'z' (122)
    char = chr(character)
    countInString1 = cleanString1.count(char)
    countInString2 = cleanString2.count(char)
    frequencyDifferences[character] = countInString1 - countInString2

# Step 5: Check if all frequency differences are non-negative
negativeFrequencyCount = 0

for difference in frequencyDifferences:
    if difference < 0:
        negativeFrequencyCount += 1

# Step 6: Output the result based on frequency check
if negativeFrequencyCount == 0:
    print("YES")
else:
    print("NO")
