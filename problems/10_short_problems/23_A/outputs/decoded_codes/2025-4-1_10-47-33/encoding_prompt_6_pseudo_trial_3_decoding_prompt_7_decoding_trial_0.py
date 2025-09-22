# Function to find the length of the longest repeated substring
def longest_repeated_substring():
    
    # Read a line of input from the user
    inputLine = input().strip()
    
    # Determine the length of the input line
    lengthOfLine = len(inputLine)
    
    # Initialize a variable to hold the result
    longestRepeatedSubstringLength = 0
    
    # Loop through possible substring lengths from 1 to lengthOfLine
    for substringLength in range(1, lengthOfLine):
        
        # Loop through each starting position in the input line
        for startIndex in range(lengthOfLine - substringLength + 1):
            
            # Extract a substring from the input line starting at startIndex with a given length
            currentSubstring = inputLine[startIndex:startIndex + substringLength]
            
            # Check if the current substring exists in the string after its starting position
            if currentSubstring in inputLine[startIndex + 1:]:
                
                # If found, update the longest repeated substring length
                longestRepeatedSubstringLength = substringLength
                break  # Stop checking other starting indices for this substring length
        
    # Output the length of the longest repeated substring found
    print(longestRepeatedSubstringLength)

# Invoke the function
longest_repeated_substring()
