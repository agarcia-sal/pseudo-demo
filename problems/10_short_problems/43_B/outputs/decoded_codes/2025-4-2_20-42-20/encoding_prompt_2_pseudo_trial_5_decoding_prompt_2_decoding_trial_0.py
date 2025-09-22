# Get Input
firstString = input()
secondString = input()

# Process Input
processedFirstString = []
processedSecondString = []

for char in firstString:
    if char != ' ':
        processedFirstString.append(char)

for char in secondString:
    if char != ' ':
        processedSecondString.append(char)

# Frequency Calculation
frequencyDifferences = []

for char_code in range(ord('A'), ord('z') + 1):
    count_first = processedFirstString.count(chr(char_code))
    count_second = processedSecondString.count(chr(char_code))
    frequencyDifferences.append(count_first - count_second)

# Condition Check and Output
if any(diff < 0 for diff in frequencyDifferences):
    print("NO")
else:
    print("YES")
