def translateSymbolString(inputString):
    # Initialize index to track position in the input string
    index = 0
    # Initialize the result string to build the output
    resultString = ""

    # Process the input string until the index reaches its length
    while index < len(inputString):
        # Check if the current character is a dot
        if inputString[index] == '.':
            # Append '0' for single dot
            resultString += '0'
            index += 1  # Move to the next character
        # Check if the next character is also a dot
        elif index + 1 < len(inputString) and inputString[index + 1] == '.':
            # Append '1' for two consecutive dots
            resultString += '1'
            index += 2  # Move past both dots
        else:
            # Append '2' for any other case (assumed to be non-dot)
            resultString += '2'
            index += 2  # Move past the current and next character

    # Return the constructed result string
    return resultString

# Read input from the standard input stream
inputString = input()

# Call the translate function and store the result
result = translateSymbolString(inputString)
# Print the result
print(result)
