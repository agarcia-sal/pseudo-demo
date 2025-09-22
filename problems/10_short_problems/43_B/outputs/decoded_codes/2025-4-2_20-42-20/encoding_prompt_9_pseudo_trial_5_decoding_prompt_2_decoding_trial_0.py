# Step 1: Receive Input
firstString = input()
secondString = input()

# Step 2: Process Input Strings
firstProcessed = firstString.replace(" ", "")
secondProcessed = secondString.replace(" ", "")

# Step 3: Initialize Frequency List
frequencyDifference = [0] * (ord('z') - ord('A') + 1)

# Step 4: Calculate Character Frequencies
for char in range(ord('A'), ord('z') + 1):
    countFirst = firstProcessed.count(chr(char))
    countSecond = secondProcessed.count(chr(char))
    frequencyDifference[char - ord('A')] = countFirst - countSecond

# Step 5: Check Conditions
negativeCount = sum(1 for diff in frequencyDifference if diff < 0)

if negativeCount == 0:
    print("YES")
else:
    print("NO")
