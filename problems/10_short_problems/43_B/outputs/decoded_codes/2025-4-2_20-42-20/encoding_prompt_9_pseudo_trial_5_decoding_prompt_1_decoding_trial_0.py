# Step 1: Receive Input
firstString = input()
secondString = input()

# Step 2: Process Input Strings
firstProcessed = firstString.replace(" ", "")
secondProcessed = secondString.replace(" ", "")

# Step 3: Initialize Frequency List
frequencyDifference = [0] * (ord('z') - ord('A') + 1)

# Step 4: Calculate Character Frequencies
for i in range(ord('A'), ord('z') + 1):  # Loop through ASCII values from 'A' to 'z'
    char = chr(i)
    countFirst = firstProcessed.count(char)
    countSecond = secondProcessed.count(char)
    frequencyDifference[i - ord('A')] = countFirst - countSecond

# Step 5: Check Conditions
negativeCount = sum(1 for difference in frequencyDifference if difference < 0)

if negativeCount == 0:
    print("YES")
else:
    print("NO")
