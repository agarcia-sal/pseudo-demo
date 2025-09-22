# Start Program

# Read Input
input_string = input().strip()

# Replace Words
modified_string = input_string.replace("dot", ".").replace("at", "@")

# Check Beginning Character
if modified_string.startswith('.'):
    modified_string = "dot" + modified_string

# Initialize Variables
countOccurrences = 0
transformedCharacters = []
length = 0  # Note: This variable is initialized but not used

# Check First Character for "at"
if modified_string.startswith('@'):
    modified_string = "at" + modified_string

# Process Each Character
for character in modified_string:
    if character == '@':
        if countOccurrences > 0:
            transformedCharacters.append('at')
            countOccurrences = 1
        else:
            transformedCharacters.append('@')
            countOccurrences = 1
    else:
        transformedCharacters.append(character)

# Combine Characters
finalEmail = ''.join(transformedCharacters)

# Check Ending Character
if finalEmail.endswith('.'):
    finalEmail = finalEmail[:-1] + 'dot'

# Output Result
print(finalEmail)

# End Program
