# Read two strings from user input, removing spaces
firstInput = input()
secondInput = input()

# Remove spaces from both inputs
cleanedFirstInput = firstInput.replace(" ", "")
cleanedSecondInput = secondInput.replace(" ", "")

# Initialize a frequency difference list to track character count differences
frequencyDifferences = []

# For each character in the range from 'A' to 'z' (ASCII values)
for characterCode in range(ord('A'), ord('z') + 1):
    # Count occurrences in each cleaned input
    countInFirstInput = cleanedFirstInput.count(chr(characterCode))
    countInSecondInput = cleanedSecondInput.count(chr(characterCode))
    
    # Calculate the difference in counts and add to the frequencyDifferences list
    frequencyDifferences.append(countInFirstInput - countInSecondInput)

# Check if all frequency differences are non-negative
nonNegativeCount = sum(1 for difference in frequencyDifferences if difference < 0)

# Output the result based on whether any negative counts were found
if nonNegativeCount == 0:
    print("YES")
else:
    print("NO")
