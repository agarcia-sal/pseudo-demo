# Read a line of input and remove any leading or trailing whitespace
stringFromUser = input().strip()

# Initialize an index variable to track our position in the string
index = 0

# Initialize an empty string to build the result
resultString = ""

# Continue processing until we have checked all characters in the input string
while index < len(stringFromUser):
    # Check if the current character is a dot ('.')
    if stringFromUser[index] == '.':
        # Append '0' to the result
        resultString += '0'
        # Move to the next character
        index += 1
    # If the next character in the string is also a dot
    elif index + 1 < len(stringFromUser) and stringFromUser[index + 1] == '.':
        # Append '1' to the result
        resultString += '1'
        # Move the index forward by two characters
        index += 2
    # If neither of the above conditions are met
    else:
        # Append '2' to the result
        resultString += '2'
        # Move the index forward by two characters
        index += 2

# Output the final constructed result string
print(resultString)
