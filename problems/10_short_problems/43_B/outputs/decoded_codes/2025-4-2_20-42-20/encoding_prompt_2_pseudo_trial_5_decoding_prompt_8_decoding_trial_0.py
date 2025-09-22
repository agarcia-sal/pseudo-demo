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

for ascii_code in range(ord('A'), ord('z') + 1):
    char = chr(ascii_code)
    countFirst = processedFirstString.count(char)
    countSecond = processedSecondString.count(char)
    difference = countFirst - countSecond
    frequencyDifferences.append(difference)

# Condition Check and Output
if any(difference < 0 for difference in frequencyDifferences):
    print("NO")
else:
    print("YES")


from collections import Counter

def process_strings(firstString, secondString):
    # Process Input
    processedFirstString = [char for char in firstString if char != ' ']
    processedSecondString = [char for char in secondString if char != ' ']

    # Frequency Calculation
    frequencyFirst = Counter(processedFirstString)
    frequencySecond = Counter(processedSecondString)

    # Collect differences
    frequencyDifferences = [
        frequencyFirst.get(chr(ascii_code), 0) - frequencySecond.get(chr(ascii_code), 0)
        for ascii_code in range(ord('A'), ord('z') + 1)
    ]

    # Condition Check and Output
    return "NO" if any(difference < 0 for difference in frequencyDifferences) else "YES"

# Get Input
firstString = input()
secondString = input()

# Output result
print(process_strings(firstString, secondString))
