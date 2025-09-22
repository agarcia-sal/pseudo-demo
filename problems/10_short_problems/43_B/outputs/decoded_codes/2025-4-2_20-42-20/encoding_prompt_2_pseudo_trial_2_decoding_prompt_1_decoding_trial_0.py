# Step 1: Receive Input
firstString = input()
secondString = input()

# Step 2: Process Input to Remove Spaces
processedFirstString = [char for char in firstString if char != ' ']
processedSecondString = [char for char in secondString if char != ' ']

# Step 3: Initialize Frequency Count
frequencyDifferences = [0] * (ord('z') - ord('A') + 1)

# Step 4: Calculate Frequency Differences
for ascii_value in range(ord('A'), ord('z') + 1):
    char = chr(ascii_value)
    count_first = processedFirstString.count(char)
    count_second = processedSecondString.count(char)
    frequencyDifferences[ascii_value - ord('A')] = count_first - count_second

# Step 5: Determine Result
if all(count >= 0 for count in frequencyDifferences):
    print("YES")
else:
    print("NO")
