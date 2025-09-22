# Input Reading
firstLine = input()
secondLine = input()

# Character Filtering
filteredFirstLine = firstLine.replace(" ", "")
filteredSecondLine = secondLine.replace(" ", "")

# Frequency Calculation
frequencyDifferences = []
for char_code in range(ord('A'), ord('z') + 1):
    char = chr(char_code)
    countFirst = filteredFirstLine.count(char)
    countSecond = filteredSecondLine.count(char)
    frequencyDifferences.append(countFirst - countSecond)

# Determine Result
if all(x >= 0 for x in frequencyDifferences):
    print("YES")
else:
    print("NO")
