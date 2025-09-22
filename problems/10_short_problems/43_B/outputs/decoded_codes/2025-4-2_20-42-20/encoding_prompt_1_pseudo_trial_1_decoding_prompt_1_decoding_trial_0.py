# Input: Read two strings from the user
firstString = input()
secondString = input()

# Process Input:
# Remove all spaces from firstString
cleanedFirst = firstString.replace(" ", "")
# Remove all spaces from secondString
cleanedSecond = secondString.replace(" ", "")

# Initialize Frequency Difference List
frequencyDifferences = []

# Count Character Frequencies:
for char in range(ord('A'), ord('z') + 1):  # ASCII range from 'A' to 'z'
    char = chr(char)  # Convert ASCII code to character
    countInFirst = cleanedFirst.count(char)  # Count in cleanedFirst
    countInSecond = cleanedSecond.count(char)  # Count in cleanedSecond
    frequencyDifferences.append(countInFirst - countInSecond)  # Append difference to list

# Check Frequency Differences:
negative_count = sum(1 for difference in frequencyDifferences if difference < 0)  # Count negative values

# Output Result:
if negative_count == 0:
    print("YES")
else:
    print("NO")
