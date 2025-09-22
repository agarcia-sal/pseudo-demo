# Get Input
firstString = input()
secondString = input()

# Process Input
processedFirstString = []
processedSecondString = []

# Add non-space characters from firstString to processedFirstString
for character in firstString:
    if character != ' ':
        processedFirstString.append(character)

# Add non-space characters from secondString to processedSecondString
for character in secondString:
    if character != ' ':
        processedSecondString.append(character)

# Frequency Calculation
frequencyDifferences = []

# Loop through ASCII values from 'A' to 'z'
for ascii_code in range(ord('A'), ord('z') + 1):
    char = chr(ascii_code)
    countFirst = processedFirstString.count(char)
    countSecond = processedSecondString.count(char)
    difference = countFirst - countSecond
    frequencyDifferences.append(difference)

# Condition Check and Output
if all(diff >= 0 for diff in frequencyDifferences):
    print("YES")
else:
    print("NO")
