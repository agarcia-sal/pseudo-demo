def main():
    # Read input line from standard input and remove the trailing newline
    inputLine = input().strip()
    lineLength = len(inputLine)
    repeatIndex = 0

    # Loop over lengths of possible substrings
    for length in range(lineLength):
        # Inner loop to check each starting position of the substring
        for startIndex in range(lineLength):
            # Create a substring of current length starting at startIndex
            currentSubstring = inputLine[startIndex:startIndex + length + 1]
            
            # Check if the substring appears in the rest of the string after startIndex
            if currentSubstring in inputLine[startIndex + 1:]:
                # Update repeatIndex to the current length if a repeat is found
                repeatIndex = length + 1  # +1 to account for zero-based index
                break  # Break out of the inner loop

    # Output the highest length of the repeated substring found
    print(repeatIndex)

# Call the main function to execute
main()
