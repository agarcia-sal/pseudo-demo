def FindLongestRepeatedSubstring(line):
    # Remove the last character from the input string
    line = RemoveLastCharacter(line)
    
    # Get the length of the input string
    n = LengthOf(line)
    
    # Initialize variable to hold the length of the longest repeated substring
    longestRepeatedLength = 0

    # Loop through substring lengths from 0 to n-1
    for length in range(n):  # Equivalent to FOR length FROM 0 TO n-1
        # Loop through each index in the input string
        for index in range(n):  # Equivalent to FOR index FROM 0 TO n-1
            # Get the current substring of the specified length starting from index
            currentSubstring = Substring(line, index, length)

            # Check if the current substring appears later in the string
            if FindSubstringIn(line, currentSubstring, index + 1) != -1:  # Instead of IS NOT -1
                # Update the length of the longest repeated substring
                longestRepeatedLength = length
                break  # Exit the inner loop if a repeated substring is found

    # Output the length of the longest repeated substring
    return longestRepeatedLength

# Helper functions
def RemoveLastCharacter(string):
    return string[:-1]  # Return the string without its last character

def LengthOf(string):
    return len(string)  # Return the length of the string

def Substring(string, startIndex, length):
    return string[startIndex:startIndex + length]  # Return the substring

def FindSubstringIn(string, substring, startIndex):
    index = string.find(substring, startIndex)  # Find the index of the substring
    return index  # Return the index or -1 if not found
