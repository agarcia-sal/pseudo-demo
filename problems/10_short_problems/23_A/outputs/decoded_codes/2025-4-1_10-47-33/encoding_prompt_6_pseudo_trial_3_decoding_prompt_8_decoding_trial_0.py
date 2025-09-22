# Read a line of input from the user and remove the trailing newline character
inputLine = input().strip()

# Determine the length of the input line
lengthOfLine = len(inputLine)

# Initialize a variable to hold the result
longestRepeatedSubstringLength = 0

# Loop through possible substring lengths from 0 to lengthOfLine - 1
for substringLength in range(lengthOfLine):
    
    # Loop through each starting position in the input line
    for startIndex in range(lengthOfLine):
        
        # Extract a substring from the input line starting at startIndex with a given length
        if startIndex + substringLength < lengthOfLine:  # Ensure we don't go out of bounds
            currentSubstring = inputLine[startIndex:startIndex + substringLength + 1]

            # Check if the current substring can be found elsewhere in the line after its starting position
            if currentSubstring in inputLine[startIndex + 1:]:
                
                # If found, update the longest repeated substring length
                longestRepeatedSubstringLength = substringLength
                break  # Stop checking other starting indices for this substring length

# Output the length of the longest repeated substring found
print(longestRepeatedSubstringLength)


    def longest_repeated_substring(input_line):
        length_of_line = len(input_line)
        longest_length = 0
        
        for substring_length in range(length_of_line):
            for start_index in range(length_of_line):
                if start_index + substring_length < length_of_line:
                    current_substring = input_line[start_index : start_index + substring_length + 1]
                    if current_substring in input_line[start_index + 1:]:
                        longest_length = substring_length
                        break
        return longest_length
    