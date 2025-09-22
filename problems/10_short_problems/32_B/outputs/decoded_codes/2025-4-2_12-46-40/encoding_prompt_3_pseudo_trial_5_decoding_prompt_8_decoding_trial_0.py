def process_string():
    # Read input from standard input and trim whitespace
    stringRepresentation = input().strip()

    # Initialize variables
    index = 0
    resultString = ""

    # Continue processing until the end of the string is reached
    while index < len(stringRepresentation):
        # Check current character at index
        if stringRepresentation[index] == '.':
            # If current character is '.', append '0' to result
            resultString += '0'
            index += 1
        elif index + 1 < len(stringRepresentation) and stringRepresentation[index + 1] == '.':
            # If the next character is also '.', append '1' to result
            resultString += '1'
            index += 2
        else:
            # If neither condition is satisfied, append '2' to result
            resultString += '2'
            index += 2

    # Output the final result string
    print(resultString)

# Example:
# process_string()
