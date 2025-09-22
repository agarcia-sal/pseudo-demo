# Step 1: Get User Input
firstString = input()
secondString = input()

# Step 2: Remove Spaces
string1 = firstString.replace(" ", "")
string2 = secondString.replace(" ", "")

# Step 3: Count Character Frequencies
frequencyDifference = []

# Loop over ASCII values from 'A' to 'z'
for char in range(ord('A'), ord('z') + 1):
    countInFirst = string1.count(chr(char))
    countInSecond = string2.count(chr(char))
    diff = countInFirst - countInSecond
    frequencyDifference.append(diff)

# Step 4: Check Frequency Differences
negativeCount = sum(1 for diff in frequencyDifference if diff < 0)

# Step 5: Generate Output
if negativeCount == 0:
    print("YES")
else:
    print("NO")
