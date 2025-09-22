# Step 1: Get Input
firstString = input()
secondString = input()

# Step 2: Process Input
processedFirstString = []
processedSecondString = []

for char in firstString:
    if char != ' ':
        processedFirstString.append(char)

for char in secondString:
    if char != ' ':
        processedSecondString.append(char)

# Step 3: Frequency Calculation
frequencyDifferences = []

for char_code in range(ord('A'), ord('z') + 1):
    countFirst = processedFirstString.count(chr(char_code))
    countSecond = processedSecondString.count(chr(char_code))
    difference = countFirst - countSecond
    frequencyDifferences.append(difference)

# Step 4: Condition Check and Output
if all(diff >= 0 for diff in frequencyDifferences):
    print("YES")
else:
    print("NO")
