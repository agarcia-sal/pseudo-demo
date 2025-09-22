# Start Program

# Receive Input:
input_string = input()  # Read a line of text from the user
if input_string.endswith('\n'):
    input_string = input_string[:-1]  # Remove last character if it is a newline
lengthOfString = len(input_string)  # Store length of the string
longestRepeatedSubstringLength = 0  # Initialize variable

# Loop Through Substring Lengths:
for currentLength in range(lengthOfString):  # From 0 to lengthOfString - 1
    for startIndex in range(lengthOfString):  # From 0 to lengthOfString - 1
        substring = input_string[startIndex:startIndex + currentLength]  # Extract substring
        # Check if this substring occurs again in the string
        if substring in input_string[startIndex + 1:]:  # Search in the rest of the string
            longestRepeatedSubstringLength = currentLength  # Update longest found
            break  # Exit inner loop to check longer substrings

# Output Result:
print(longestRepeatedSubstringLength)  # Print the length of the longest repeated substring

# End Program
