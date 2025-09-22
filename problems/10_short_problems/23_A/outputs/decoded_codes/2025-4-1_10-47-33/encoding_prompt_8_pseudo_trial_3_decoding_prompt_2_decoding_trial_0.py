def main():
    # Read a line of input
    inputString = input().rstrip('\n')  # Exclude the last character (newline)
    
    # Get the length of the input string
    stringLength = len(inputString)
    
    # Initialize a variable to store the result
    longestPrefixLength = 0

    # Loop through potential prefix lengths from 0 up to stringLength - 1
    for currentLength in range(stringLength):  # currentLength from 0 to stringLength - 1
        
        # Check every starting position in the string
        for startPosition in range(stringLength):  # startPosition from 0 to stringLength - 1
            
            # Get the current prefix substring
            prefixSubstring = inputString[startPosition:startPosition + currentLength]
            
            # Check if the prefixSubstring exists again elsewhere in the string
            if inputString.find(prefixSubstring, startPosition + 1) != -1:  # Start search after the current prefix
                # Update the longest prefix length if a match is found
                longestPrefixLength = currentLength
                break  # Exit the inner loop if a match is found

    # Output the length of the longest prefix found
    print(longestPrefixLength)

# Call main function to execute the code
main()
