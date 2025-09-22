# Begin program

# Read two input strings from the user
firstInput = input()  # User input for the first string
secondInput = input()  # User input for the second string

# Remove spaces from both input strings
firstProcessedString = [char for char in firstInput if char != ' ']  # List of characters excluding spaces
secondProcessedString = [char for char in secondInput if char != ' ']  # List of characters excluding spaces

# Initialize a frequency list to hold character count differences
# ASCII characters range from 'A' (65) to 'z' (122), hence the size will be 123
characterFrequencyDifferences = [0] * 123  # List of zeroes for ASCII characters

# Calculate the differences in character frequencies between the two strings
for ascii_value in range(65, 123):  # Iterating from ASCII value of 'A' to 'z'
    currentCharacter = chr(ascii_value)  # Get the character from ASCII value
    countInFirstString = firstProcessedString.count(currentCharacter)  # Count occurrences in first string
    countInSecondString = secondProcessedString.count(currentCharacter)  # Count occurrences in second string
    frequencyDifference = countInFirstString - countInSecondString  # Calculate frequency difference
    characterFrequencyDifferences[ascii_value] = frequencyDifference  # Store the difference in the list

# Check if there are any negative differences in the frequency
negativeCount = sum(1 for difference in characterFrequencyDifferences if difference < 0)  # Count negative differences

# Determine the final output based on negative counts
if negativeCount == 0:  # If there are no negative differences
    print("YES")  # Output YES
else:
    print("NO")  # Output NO

# End program
