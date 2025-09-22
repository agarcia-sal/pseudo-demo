def countOccurrences(targetChar, characterList):
    # Helper function to count occurrences of a character in a character list
    count = 0
    for character in characterList:
        if character == targetChar:
            count += 1
    return count

# Step 1: Accept input
firstString = input()
secondString = input()

# Step 2: Remove spaces from both strings
cleanedString1 = []
cleanedString2 = []

for character in firstString:
    if character != ' ':
        cleanedString1.append(character)

for character in secondString:
    if character != ' ':
        cleanedString2.append(character)

# Step 3: Calculate frequency differences of characters
frequencyDifferences = []

for ascii_value in range(ord('A'), ord('z') + 1):
    currentChar = chr(ascii_value)
    countInFirst = countOccurrences(currentChar, cleanedString1)
    countInSecond = countOccurrences(currentChar, cleanedString2)
    frequencyDifferences.append(countInFirst - countInSecond)

# Step 4: Check if there are any negative frequency differences
hasNegativeFrequency = False
for difference in frequencyDifferences:
    if difference < 0:
        hasNegativeFrequency = True
        break

# Step 5: Output result
if not hasNegativeFrequency:
    print("YES")
else:
    print("NO")
