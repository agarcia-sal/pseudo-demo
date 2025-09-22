# Step 1: Get User Input
firstString = input()
secondString = input()

# Step 2: Prepare Strings
preparedFirstString = [char for char in firstString if char != ' ']
preparedSecondString = [char for char in secondString if char != ' ']

# Step 3: Count Character Frequencies
characterFrequencyDifference = []
for char in range(ord('A'), ord('z') + 1):
    char = chr(char)  # Convert ASCII value back to character
    countFirst = preparedFirstString.count(char)
    countSecond = preparedSecondString.count(char)
    characterFrequencyDifference.append(countFirst - countSecond)

# Step 4: Check Character Frequency Differences
negativeCount = sum(1 for diff in characterFrequencyDifference if diff < 0)

# Step 5: Determine Result
if negativeCount == 0:
    print("YES")
else:
    print("NO")
