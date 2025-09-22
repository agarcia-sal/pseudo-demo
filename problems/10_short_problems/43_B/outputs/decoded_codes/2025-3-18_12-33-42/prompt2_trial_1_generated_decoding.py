# Receive Input
firstInput = input()
secondInput = input()

# Process Strings
processedFirstString = firstInput.replace(" ", "")
processedSecondString = secondInput.replace(" ", "")

# Calculate Frequency Differences
frequencyDifferences = []
for char_code in range(ord('A'), ord('z') + 1):
    char = chr(char_code)
    countInFirst = processedFirstString.count(char)
    countInSecond = processedSecondString.count(char)
    difference = countInFirst - countInSecond
    frequencyDifferences.append(difference)

# Check for Negative Differences
negativeCount = sum(1 for diff in frequencyDifferences if diff < 0)

# Output Result
if negativeCount == 0:
    print("YES")
else:
    print("NO")
