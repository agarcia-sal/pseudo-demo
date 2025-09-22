# Read a line of input and remove any leading/trailing whitespace
inputString = input().strip()

# Initialize a variable to track our position within inputString
index = 0

# Initialize an empty string to hold the final output
result = ""

# Process the input string character by character
while index < len(inputString):
    # Check if the current character is a dot
    if inputString[index] == '.':
        result += '0'  # Append '0' if current character is a dot
        index += 1     # Move to the next character
    
    else:
        # Check the character immediately following the current one
        if index + 1 < len(inputString) and inputString[index + 1] == '.':
            result += '1'  # Append '1' if the following character is a dot
            index += 2     # Move forward by two characters
        else:
            result += '2'  # Append '2' if the following character is not a dot
            index += 2     # Move forward by two characters

# Output the final result
print(result)
