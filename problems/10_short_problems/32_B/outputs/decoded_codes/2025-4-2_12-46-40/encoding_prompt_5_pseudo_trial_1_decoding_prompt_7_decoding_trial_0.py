# Begin the program

# Accept input string from the user
inputString = input()  # Read the input string
inputString = inputString.strip()  # Trim whitespace from both ends

# Initialize an index variable and an empty result string
index = 0
resultString = ''

# Loop through the characters in the input string
while index < len(inputString):  # Continue until the end of the string
    
    # Check if the current character is a dot
    if inputString[index] == '.':  # If the current character is a dot
        resultString += '0'  # Append '0' to the result string
        index += 1  # Move to the next character

    # Check if the current character is not a dot and next character is a dot
    elif index + 1 < len(inputString) and inputString[index + 1] == '.':  # Ensure next index is valid
        resultString += '1'  # Append '1' to the result string
        index += 2  # Skip the next character (since it's also a dot)

    else:  # If the next character is neither a dot nor out of bounds
        resultString += '2'  # Append '2' to the result string
        index += 2  # Skip to the next possible character pair

# Print the final result string
print(resultString)  # Output the result string
