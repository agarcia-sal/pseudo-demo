# Step 1: Receive Input
firstString = input()
secondString = input()

# Step 2: Process Input to Remove Spaces
processedFirstString = [char for char in firstString if char != ' ']
processedSecondString = [char for char in secondString if char != ' ']

# Step 3: Initialize Frequency Count
frequencyDifferences = [0] * 123  # ASCII range from 'A' (65) to 'z' (122)

# Step 4: Calculate Frequency Differences
for ascii_value in range(65, 123):  # ASCII values for 'A' to 'z'
    char = chr(ascii_value)
    countInFirst = processedFirstString.count(char)
    countInSecond = processedSecondString.count(char)
    frequencyDifferences[ascii_value] = countInFirst - countInSecond

# Step 5: Determine Result
if all(count >= 0 for count in frequencyDifferences):
    print("YES")
else:
    print("NO")
