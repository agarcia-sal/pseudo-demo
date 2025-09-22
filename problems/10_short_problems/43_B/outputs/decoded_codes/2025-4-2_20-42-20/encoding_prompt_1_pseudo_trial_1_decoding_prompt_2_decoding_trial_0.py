# Input: Read two strings from the user
firstString = input()
secondString = input()

# Process Input: Remove all spaces from both strings
cleanedFirst = firstString.replace(" ", "")
cleanedSecond = secondString.replace(" ", "")

# Initialize Frequency Difference List
frequencyDifferences = []

# Count Character Frequencies
for char in range(ord('A'), ord('z') + 1):
    countInFirst = cleanedFirst.count(chr(char))
    countInSecond = cleanedSecond.count(chr(char))
    difference = countInFirst - countInSecond
    frequencyDifferences.append(difference)

# Check Frequency Differences
negativeCount = sum(1 for diff in frequencyDifferences if diff < 0)

# Output Result
if negativeCount == 0:
    print("YES")
else:
    print("NO")
