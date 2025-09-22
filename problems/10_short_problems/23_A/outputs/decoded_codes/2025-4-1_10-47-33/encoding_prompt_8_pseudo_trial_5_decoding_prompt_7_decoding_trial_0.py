# Start of the program to find the length of the longest repeated substring

# Read the input line from the user and remove the last character (usually a newline).
inputLine = input().strip()  # .strip() removes any leading/trailing whitespace, including newlines

# Calculate the length of the input line.
lengthOfInput = len(inputLine)

# Initialize a variable to keep track of the maximum length of substrings found.
longestRepeatedSubstringLength = 0

# Loop through all possible lengths of substrings, starting from 1 to length of the input line.
for substringLength in range(1, lengthOfInput):  # start from 1 since we are looking for repeats
    # Loop through each starting position in the string for a substring of the current length.
    for startIndex in range(lengthOfInput - substringLength + 1):
        
        # Extract the substring from the input string starting at startIndex with the current length.
        currentSubstring = inputLine[startIndex:startIndex + substringLength]

        # Check if this substring appears again in the input string, starting from the position after startIndex.
        if inputLine.find(currentSubstring, startIndex + 1) != -1:
            # If found, update the longest substring length variable.
            longestRepeatedSubstringLength = substringLength
            
            # Break out of the loop as we only need the longest length for this size.
            break  # Exit the inner loop to look for longer substrings in the next iteration

# Output the maximum length of the repeated substring found.
print(longestRepeatedSubstringLength)

# End of the program
