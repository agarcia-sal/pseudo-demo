# Step 1: Receive Input
firstString = input()
secondString = input()

# Step 2: Process Input to Remove Spaces
processedFirstString = [char for char in firstString if char != ' ']
processedSecondString = [char for char in secondString if char != ' ']

# Step 3: Initialize Frequency Count
frequencyDifferences = [0] * (ord('z') - ord('A') + 1)

# Step 4: Calculate Frequency Differences
for char_code in range(ord('A'), ord('z') + 1):
    char = chr(char_code)
    countFirst = processedFirstString.count(char)
    countSecond = processedSecondString.count(char)
    frequencyDifferences[char_code - ord('A')] = countFirst - countSecond

# Step 5: Determine Result
if all(count >= 0 for count in frequencyDifferences):
    print("YES")
else:
    print("NO")
