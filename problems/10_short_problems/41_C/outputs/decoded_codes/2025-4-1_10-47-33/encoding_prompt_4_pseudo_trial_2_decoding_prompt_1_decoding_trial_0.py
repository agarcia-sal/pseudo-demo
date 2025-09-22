# BEGIN

# Read input from the user
userInput = input()

# Replace occurrences of 'dot' with '.' and 'at' with '@'
userInput = userInput.replace('dot', '.')
userInput = userInput.replace('at', '@')

# If the first character is '.', prepend 'dot'
if userInput[0] == '.':
    userInput = 'dot' + userInput[1:]

# Initialize count for '@' symbols and a list to hold characters
atCount = 0
characterList = []

# If the first character is '@', prepend 'at'
if userInput[0] == '@':
    userInput = 'at' + userInput[1:]

# Iterate over each character in the modified input
for character in userInput:
    
    # Check if the character is '@'
    if character == '@':
        if atCount > 0:
            # Append 'at' if it's not the first '@'
            characterList.append('at')
            atCount = 1
        else:
            # Append first '@' as is
            characterList.append('@')
            atCount = 1
    else:
        # Append non '@' characters to the list
        characterList.append(character)

# Join the character list into a single string
finalOutput = ''.join(characterList)

# If the last character is '.', replace it with 'dot'
if finalOutput[-1] == '.':
    finalOutput = finalOutput[:-1] + 'dot'

# Output the final modified string
print(finalOutput)

# END
