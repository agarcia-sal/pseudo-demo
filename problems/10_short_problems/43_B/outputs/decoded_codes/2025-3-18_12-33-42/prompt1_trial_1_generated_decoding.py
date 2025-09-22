# Get Input
firstString = input()
secondString = input()

# Prepare Strings
cleanedFirstString = [char for char in firstString if char != ' ']
cleanedSecondString = [char for char in secondString if char != ' ']

# Initialize Frequency Difference List
frequencyDifferences = []

# Calculate Frequency Differences
for ascii_value in range(65, 123):  # range(65, 123) goes from 65 to 122
    char = chr(ascii_value)
    countInFirst = cleanedFirstString.count(char)
    countInSecond = cleanedSecondString.count(char)
    difference = countInFirst - countInSecond
    frequencyDifferences.append(difference)

# Check Conditions
negative_count = sum(1 for value in frequencyDifferences if value < 0)
if negative_count == 0:
    print("YES")
else:
    print("NO")
