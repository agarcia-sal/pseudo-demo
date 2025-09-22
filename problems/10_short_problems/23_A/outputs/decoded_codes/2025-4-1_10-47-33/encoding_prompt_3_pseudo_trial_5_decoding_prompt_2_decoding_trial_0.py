def main():
    # Read input line from standard input and remove the trailing newline
    inputLine = input().strip()
    lineLength = len(inputLine)
    repeatIndex = 0

    # Loop over lengths of possible substrings
    for length in range(1, lineLength):  # Starting from 1 to avoid empty substrings
        # Inner loop to check each starting position of the substring
        for startIndex in range(lineLength - length + 1): 
            # Create a substring of current length starting at startIndex
            currentSubstring = inputLine[startIndex:startIndex + length]

            # Check if the substring appears in the rest of the string after startIndex
            if currentSubstring in inputLine[startIndex + 1:]:
                # Update repeatIndex to the current length if a repeat is found
                repeatIndex = length
                break  # Exit the inner loop if a repeat is found
    
    # Output the highest length of the repeated substring found
    print(repeatIndex)

# Call the main function
main()
