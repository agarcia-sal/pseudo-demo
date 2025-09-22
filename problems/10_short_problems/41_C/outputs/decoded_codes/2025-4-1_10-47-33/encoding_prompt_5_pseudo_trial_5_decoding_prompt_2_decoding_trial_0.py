# BEGIN PROGRAM

# Read input from the standard input and remove trailing spaces
inputString = input().rstrip()  # Read input and remove trailing spaces
originalString = inputString      # Store the original string

# Replace occurrences in the string
originalString = originalString.replace("dot", ".")
originalString = originalString.replace("at", "@")

# Check if the first character is a dot
if originalString.startswith("."):
    originalString = "dot" + originalString  # Prepend "dot" if it starts with a dot

# Initialize variables to manage email formatting
previousChar = 0  # To track the last occurrence of '@'
formattedCharacters = []  # Create an empty list for formatted characters
lengthToLastChar = 0  # To hold the length of the formatted string

# Check if the string starts with an '@'
if originalString.startswith("@"):
    originalString = "at" + originalString  # Prepend "at" if it starts with an '@'

# Iterate through each character in the modified string
for character in originalString:
    # Check if the character is an '@'
    if character == "@":
        if previousChar > 0:
            formattedCharacters.append("at")  # Replace '@' with 'at' if previous was also '@'
            previousChar = 1  # Update to indicate '@' was found
        else:
            formattedCharacters.append("@")  # Append '@' to the list
            previousChar = 1  # Update to indicate '@' was found
    else:
        formattedCharacters.append(character)  # Append other characters directly

# Join the formatted characters into a single string
finalString = ''.join(formattedCharacters)  # Create the final formatted string

# Check if the last character of the formatted string is a dot
if finalString.endswith("."):
    finalString = finalString[:-1] + "dot"  # Replace the last character if it's a dot

# Print the final formatted string
print(finalString)  # Output the final string

# END PROGRAM
