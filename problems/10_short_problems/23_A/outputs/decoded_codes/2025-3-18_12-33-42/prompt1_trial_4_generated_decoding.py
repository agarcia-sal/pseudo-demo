# Function to read a line of input and find the length of the longest repeating substring
def find_longest_repeating_substring():
    # Read a line of input
    inputLine = input()
    lengthOfInputLine = len(inputLine)  # Calculate the length of the input line
    resultValue = 0  # Initialize a variable to hold the result

    # Loop through all possible substring lengths from 0 to the length of the input line
    for substringLength in range(lengthOfInputLine + 1):
        # Loop through the input line to examine each starting position of the substring
        for startIndex in range(lengthOfInputLine):
            # Extract a substring of the current length starting from startIndex
            substring = inputLine[startIndex:startIndex + substringLength]

            # Check if the extracted substring occurs again in the input line after its current position
            if substring in inputLine[startIndex + 1:]:  # Check substring in the rest of the string
                # If found, set the resultValue to the length of the substring
                resultValue = substringLength
                
                # Exit the inner loop as we found a repeating substring
                break

    # Output the result value which holds the maximum length of the repeating substring
    print(resultValue)

# Call the function
find_longest_repeating_substring()
