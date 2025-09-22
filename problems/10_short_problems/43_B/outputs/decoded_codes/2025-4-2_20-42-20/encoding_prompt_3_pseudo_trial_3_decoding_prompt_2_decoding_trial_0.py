# Step 1: Read input
firstString = input()
secondString = input()

# Step 2: Remove spaces from both strings
filteredFirstString = []
filteredSecondString = []

for character in firstString:
    if character != ' ':
        filteredFirstString.append(character)

for character in secondString:
    if character != ' ':
        filteredSecondString.append(character)

# Step 3: Count character frequency differences
frequencyDifferences = []

# ASCII range from 'A' (65) to 'z' (122)
for characterCode in range(ord('A'), ord('z') + 1):
    character = chr(characterCode)
    countInFirstString = filteredFirstString.count(character)
    countInSecondString = filteredSecondString.count(character)
    difference = countInFirstString - countInSecondString
    frequencyDifferences.append(difference)

# Step 4: Check if any frequency difference is negative
hasNegativeDifference = False

for difference in frequencyDifferences:
    if difference < 0:
        hasNegativeDifference = True
        break

# Step 5: Output the result
if not hasNegativeDifference:
    print("YES")
else:
    print("NO")
