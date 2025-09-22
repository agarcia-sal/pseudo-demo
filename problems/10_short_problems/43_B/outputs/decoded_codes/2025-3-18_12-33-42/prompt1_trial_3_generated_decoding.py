# 1. Get Input
firstString = input()
secondString = input()

# 2. Process Strings
cleanedFirstString = [char for char in firstString if char != ' ']
cleanedSecondString = [char for char in secondString if char != ' ']

# 3. Initialize Frequency List
frequencyDifference = []

for char_code in range(ord('A'), ord('z') + 1):  # Iterate over character codes from 'A' to 'z'
    char = chr(char_code)  # Convert character code back to character
    countFirst = cleanedFirstString.count(char)  # Count occurrences in the first string
    countSecond = cleanedSecondString.count(char)  # Count occurrences in the second string
    difference = countFirst - countSecond  # Calculate the difference
    frequencyDifference.append(difference)  # Add the difference to the list

# 4. Check Frequency Differences
negativeCount = sum(1 for diff in frequencyDifference if diff < 0)  # Count negative differences

if negativeCount == 0:
    print("YES")
else:
    print("NO")
