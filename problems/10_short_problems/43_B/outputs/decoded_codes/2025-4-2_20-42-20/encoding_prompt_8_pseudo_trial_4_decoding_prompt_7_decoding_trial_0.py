# Initialize Variables
# List to store the first input string after removing spaces
firstInput = []
# List to store the second input string after removing spaces
secondInput = []

# Get Input from User
# Read the first input string, removing spaces and converting to a list of characters
firstInput = list(input().replace(" ", ""))
# Read the second input string, removing spaces and converting to a list of characters
secondInput = list(input().replace(" ", ""))

# Count Characters Frequency
# Create a list to hold the frequency difference of characters
characterFrequencyDifference = []

# Loop through ASCII values for characters
for char in range(65, 123):  # ASCII range from 'A' (65) to 'z' (122)
    charFromFirst = firstInput.count(chr(char))  # Count in firstInput
    charFromSecond = secondInput.count(chr(char))  # Count in secondInput
    
    # Calculate the difference in counts and add to characterFrequencyDifference
    characterFrequencyDifference.append(charFromFirst - charFromSecond)

# Evaluate Results
# Count how many values in characterFrequencyDifference are negative
negativeCount = sum(1 for diff in characterFrequencyDifference if diff < 0)

# Output the result based on negative counts
if negativeCount == 0:  # If no character is less in firstInput than in secondInput
    print("YES")
else:
    print("NO")
