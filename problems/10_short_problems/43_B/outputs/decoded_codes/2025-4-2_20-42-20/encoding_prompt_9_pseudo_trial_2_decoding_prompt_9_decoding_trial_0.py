# Receive two strings from the user
firstString = input()
secondString = input()

# Remove spaces from both strings
firstString = firstString.replace(" ", "")
secondString = secondString.replace(" ", "")

# Initialize frequency count list for character differences
# We will assume characters are in the range of ASCII values 65 to 122 (A to z)
characterDifferences = [0] * (123)  # 123 covers ASCII characters from 0 to 122

# Count character frequencies in both strings
for char in range(65, 123):  # ASCII for 'A' is 65, 'z' is 122
    countInFirst = firstString.count(chr(char))
    countInSecond = secondString.count(chr(char))
    characterDifferences[char] = countInFirst - countInSecond

# Check if all values in characterDifferences are non-negative
allNonNegative = True
for difference in characterDifferences:
    if difference < 0:  # If any character is in deficit
        allNonNegative = False
        break

# Output the result
if allNonNegative:
    print("YES")
else:
    print("NO")
