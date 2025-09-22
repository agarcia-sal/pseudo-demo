# Read two input strings from the user
firstInput = input()
secondInput = input()

# Remove spaces from both input strings
firstProcessedString = [char for char in firstInput if char != ' ']
secondProcessedString = [char for char in secondInput if char != ' ']

# Initialize a frequency list to hold character count differences
characterFrequencyDifferences = [0] * 256  # Considering extended ASCII

# Calculate the differences in character frequencies between the two strings
for ascii_value in range(65, 123):  # From 'A' (65) to 'z' (122)
    currentCharacter = chr(ascii_value)
    countInFirstString = firstProcessedString.count(currentCharacter)
    countInSecondString = secondProcessedString.count(currentCharacter)
    frequencyDifference = countInFirstString - countInSecondString
    characterFrequencyDifferences[ascii_value] = frequencyDifference

# Check if there are any negative differences in the frequency
negativeCount = sum(1 for diff in characterFrequencyDifferences if diff < 0)

# Determine the final output based on negative counts
if negativeCount == 0:
    print("YES")  # There are no negative frequency differences
else:
    print("NO")   # There are negative frequency differences
