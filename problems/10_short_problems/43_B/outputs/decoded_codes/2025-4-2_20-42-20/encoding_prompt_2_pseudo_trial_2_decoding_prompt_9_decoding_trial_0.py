# Read two strings from the user input
firstString = input()
secondString = input()

# Remove spaces from each string
processedFirstString = [char for char in firstString if char != ' ']
processedSecondString = [char for char in secondString if char != ' ']

# Initialize frequency differences for characters 'A' to 'z'
frequencyDifferences = [0] * (ord('z') - ord('A') + 1)

# Calculate frequency differences
for ascii_value in range(ord('A'), ord('z') + 1):
    char = chr(ascii_value)
    countInFirst = processedFirstString.count(char)
    countInSecond = processedSecondString.count(char)
    frequencyDifferences[ascii_value - ord('A')] = countInFirst - countInSecond

# Determine the result based on the frequency differences
if all(count >= 0 for count in frequencyDifferences):
    print("YES")
else:
    print("NO")
