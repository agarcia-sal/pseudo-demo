# Step 1: Receive Input
firstString = input()
secondString = input()

# Step 2: Process Input Strings
firstProcessed = firstString.replace(" ", "")
secondProcessed = secondString.replace(" ", "")

# Step 3: Initialize Frequency List
frequencyDifference = [0] * (ord('z') - ord('A') + 1)

# Step 4: Calculate Character Frequencies
for i in range(ord('A'), ord('z') + 1):
    countFirst = firstProcessed.count(chr(i))
    countSecond = secondProcessed.count(chr(i))
    frequencyDifference[i - ord('A')] = countFirst - countSecond

# Step 5: Check Conditions
if all(diff >= 0 for diff in frequencyDifference):
    print("YES")
else:
    print("NO")


from collections import Counter

# Step 1: Receive Input
firstString = input()
secondString = input()

# Step 2: Process Input Strings
firstProcessed = firstString.replace(" ", "")
secondProcessed = secondString.replace(" ", "")

# Step 3: Calculate Character Frequencies
firstCount = Counter(firstProcessed)
secondCount = Counter(secondProcessed)

# Step 4: Check Conditions
for char in secondCount:
    if firstCount[char] < secondCount[char]:
        print("NO")
        break
else:
    print("YES")
