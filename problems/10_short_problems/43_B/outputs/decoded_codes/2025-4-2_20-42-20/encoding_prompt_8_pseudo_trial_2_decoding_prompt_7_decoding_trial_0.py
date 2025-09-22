# Step 1: Gather Input Strings
# Read the first and second strings from user input
first_input = input()
second_input = input()

# Step 2: Process Strings to Remove Spaces
# Create lists of characters from the input strings excluding spaces
firstString = [char for char in first_input if char != ' ']
secondString = [char for char in second_input if char != ' ']

# Step 3: Calculate Frequency Differences
# Initialize a list to store frequency differences
# The list will have 58 entries: from 'A' (ASCII 65) to 'z' (ASCII 122)
frequencyDifferences = [0] * 58

# Loop through each character code from 'A' (65) to 'z' (122)
for char_code in range(65, 123):
    # Calculate the character based on ASCII code
    char = chr(char_code)

    # Count occurrences in firstString
    count_first = firstString.count(char)
    # Count occurrences in secondString
    count_second = secondString.count(char)

    # Calculate the difference (first minus second) and store it
    frequencyDifferences[char_code - 65] = count_first - count_second

# Step 4: Determine Validity of Transformation
# Check if there are any negative values in the frequencyDifferences list
can_transform = all(diff >= 0 for diff in frequencyDifferences)

# Step 5: Output the Result
# Print "YES" if transformation is possible, otherwise print "NO"
if can_transform:
    print("YES")
else:
    print("NO")
