# BEGIN

# Read two input strings from the user
firstInput = input()
secondInput = input()

# Remove spaces from both input strings
firstProcessedString = [char for char in firstInput if char != ' ']
secondProcessedString = [char for char in secondInput if char != ' ']

# Initialize a frequency list to hold character count differences
# Create a list of zeroes for each ASCII character from 'A' (65) to 'z' (122)
characterFrequencyDifferences = [0] * (123)  # ASCII values from 0 to 122

# Calculate the differences in character frequencies between the two strings
for asciiValue in range(65, 123):  # From 'A' (65) to 'z' (122)
    currentCharacter = chr(asciiValue)  # Get character from ASCII value
    countInFirstString = firstProcessedString.count(currentCharacter)
    countInSecondString = secondProcessedString.count(currentCharacter)
    
    frequencyDifference = countInFirstString - countInSecondString
    characterFrequencyDifferences[asciiValue] = frequencyDifference

# Check if there are any negative differences in the frequency
negativeCount = sum(1 for difference in characterFrequencyDifferences if difference < 0)

# Determine the final output based on negative counts
if negativeCount == 0:
    print("YES")  # There are no negative frequency differences
else:
    print("NO")   # There are negative frequency differences

# END
