# Start Program

# Read Input
user_input = input().strip()  # Get a line of text and remove extra spaces

# Replace Words with Symbols
modified_text = user_input.replace("dot", ".").replace("at", "@")

# Check for Leading Symbols
if modified_text and modified_text[0] == '.':
    modified_text = "dot " + modified_text  # Prepend "dot" if leading is '.'

# Initialize Variables
symbolCounter = 0
resultList = []

# Check for Leading '@' Symbol
if modified_text and modified_text[0] == '@':
    modified_text = "at " + modified_text  # Prepend "at" if leading is '@'

# Processing Each Character
for char in modified_text:
    if char == '@':
        if symbolCounter > 0:  # If we already added an '@' before
            resultList.append("at")  # Append "at"
            symbolCounter = 1  # Indicate the last added symbol is now 'at'
        else:
            resultList.append('@')  # Append '@'
            symbolCounter = 1  # Indicate the last added symbol is now '@'
    else:
        resultList.append(char)  # Append the character

# Join Resulting Characters
finalString = ''.join(resultList)  # Combine elements into a single string

# Check for Trailing Symbols
if finalString and finalString[-1] == '.':
    finalString = finalString[:-1] + "dot"  # Replace trailing '.' with "dot"

# Output Result
print(finalString)  # Display the final string to the user

# End Program
