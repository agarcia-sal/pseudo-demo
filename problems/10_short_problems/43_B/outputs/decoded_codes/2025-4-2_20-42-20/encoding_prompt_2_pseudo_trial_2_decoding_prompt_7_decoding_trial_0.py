# Receive Input
firstString = input()  # Read the first string from user input
secondString = input()  # Read the second string from user input

# Process Input to Remove Spaces
processedFirstString = [char for char in firstString if char != ' ']  # Remove spaces from firstString
processedSecondString = [char for char in secondString if char != ' ']  # Remove spaces from secondString

# Initialize Frequency Count
frequencyDifferences = [0] * (ord('z') - ord('A') + 1)  # Initialize a list to keep track of frequency differences

# Calculate Frequency Differences
for ascii_value in range(ord('A'), ord('z') + 1):  # Loop through ASCII values from 'A' to 'z'
    char = chr(ascii_value)  # Convert ASCII value back to character
    countFirst = processedFirstString.count(char)  # Count occurrences in first string
    countSecond = processedSecondString.count(char)  # Count occurrences in second string
    frequencyDifferences[ascii_value - ord('A')] = countFirst - countSecond  # Store the difference

# Determine Result
if all(count >= 0 for count in frequencyDifferences):  # Check if all counts are non-negative
    print("YES")  # If all counts are non-negative, print YES
else:
    print("NO")  # If any count is negative, print NO
