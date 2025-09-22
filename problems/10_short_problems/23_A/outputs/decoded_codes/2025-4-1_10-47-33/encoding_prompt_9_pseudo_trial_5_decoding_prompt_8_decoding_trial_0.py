# Step 1: Get the Input
text_input = input().rstrip()  # Read a line of text and remove trailing newline
stringLength = len(text_input)  # Store length of the input string
longestRepeatedSubstringLength = 0  # Initialize maximum length of repeated substring

# Step 2: Iterate Over Possible Substring Lengths
for currentLength in range(1, stringLength):  # Loop from 1 to stringLength - 1
    for startPosition in range(stringLength - currentLength):  # Loop from 0 to stringLength - currentLength
        substring = text_input[startPosition:startPosition + currentLength]  # Extract substring
        # Check if the substring appears again in the remainder of the string
        if substring in text_input[startPosition + 1:]:  # Search starting after the current position
            longestRepeatedSubstringLength = currentLength  # Update the longest length found
            break  # Exit inner loop if a repeated substring is found

# Step 3: Output the Length
print(longestRepeatedSubstringLength)  # Output the length of the longest repeated substring


def longest_repeated_substring_length(text):
    # Function implementation here...
