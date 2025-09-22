# Read two strings from the user
firstString = input()
secondString = input()

# Remove all spaces from firstString and store the result in cleanedFirst
cleanedFirst = firstString.replace(" ", "")

# Remove all spaces from secondString and store the result in cleanedSecond
cleanedSecond = secondString.replace(" ", "")

# Initialize the frequency differences list
frequencyDifferences = []

# Count character frequencies
for char in range(ord('A'), ord('z') + 1):
    # Convert the ASCII value back to character
    character = chr(char)

    # Count occurrences in cleanedFirst
    countInFirst = cleanedFirst.count(character)

    # Count occurrences in cleanedSecond
    countInSecond = cleanedSecond.count(character)

    # Calculate the difference and append to frequencyDifferences
    frequencyDifferences.append(countInFirst - countInSecond)

# Check frequency differences for negative values
negativeCount = sum(1 for difference in frequencyDifferences if difference < 0)

# Output result
if negativeCount == 0:
    print("YES")
else:
    print("NO")
