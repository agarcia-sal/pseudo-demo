def translateDotsAndDashes(inputString):
    # Initialize the index to keep track of our position in the input string
    index = 0
    # Initialize an empty string to store the result
    answer = ""
    
    # Loop through the string until we've processed all characters
    while index < len(inputString):
        # Check if the current character is a dot
        if inputString[index] == '.':
            answer += '0'  # Append '0' for a single dot
            index += 1     # Move to the next character
        # Check if the next character is also a dot
        elif index + 1 < len(inputString) and inputString[index + 1] == '.':
            answer += '1'  # Append '1' for two consecutive dots
            index += 2     # Move past both dots
        else:
            answer += '2'  # Append '2' for any other character (such as a dash)
            index += 2     # Move past the character that represents '2'

    return answer  # Return the accumulated result

# Read input from standard input
inputString = input()  # Get the input string
result = translateDotsAndDashes(inputString)  # Call the translation function
print(result)  # Output the result
