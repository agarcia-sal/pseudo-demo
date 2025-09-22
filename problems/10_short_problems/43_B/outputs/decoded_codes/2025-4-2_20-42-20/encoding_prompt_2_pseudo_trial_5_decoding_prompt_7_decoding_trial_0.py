# Step 1: Get Input
# Read two lines of input and store them as strings
firstString = input()
secondString = input()

# Step 2: Process Input
# Create lists to hold processed characters
processedFirstString = []
processedSecondString = []

# Process the first string, adding non-space characters to the list
for char in firstString:
    if char != ' ':  # Check if the character is not a space
        processedFirstString.append(char)

# Process the second string, adding non-space characters to the list
for char in secondString:
    if char != ' ':  # Check if the character is not a space
        processedSecondString.append(char)

# Step 3: Frequency Calculation
# Create a list to store frequency differences
frequencyDifferences = []

# Loop through ASCII values from 'A' (65) to 'z' (122)
for code in range(65, 123):  # 65 is 'A' and 122 is 'z'
    # Count occurrences in both processed strings
    countFirst = processedFirstString.count(chr(code))
    countSecond = processedSecondString.count(chr(code))
    
    # Calculate the difference and store it
    difference = countFirst - countSecond
    frequencyDifferences.append(difference)

# Step 4: Condition Check and Output
# Check for negative values in frequencyDifferences
if all(diff >= 0 for diff in frequencyDifferences):  # Check if all values are non-negative
    print("YES")  # Print YES if there are no negative values
else:
    print("NO")   # Print NO if there is at least one negative value
