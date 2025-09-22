# Step 1: Input
firstString = input()
secondString = input()

# Step 2: Process Input
cleanedFirst = firstString.replace(" ", "")
cleanedSecond = secondString.replace(" ", "")

# Step 3: Initialize Frequency Difference List
frequencyDifferences = []

# Step 4: Count Character Frequencies
for char in range(ord('A'), ord('z') + 1):
    countInFirst = cleanedFirst.count(chr(char))
    countInSecond = cleanedSecond.count(chr(char))
    frequencyDifferences.append(countInFirst - countInSecond)

# Step 5: Check Frequency Differences
negativeCount = sum(1 for diff in frequencyDifferences if diff < 0)

# Step 6: Output Result
if negativeCount == 0:
    print("YES")
else:
    print("NO")
