# Start Program

# Read Input
input_string = input().strip()

# Replace Specific Words
input_string = input_string.replace("dot", ".").replace("at", "@")

# Ensure Proper Start Character
if input_string and input_string[0] == ".":
    input_string = "dot" + input_string

# Initialize Variables
counter = 0
characterList = []
length = 0  # This variable is defined but not used

# Check for Starting "at" Character
if input_string and input_string[0] == "@":
    input_string = "at" + input_string[1:]

# Process Each Character in the String
for character in input_string:
    if character == "@":
        if counter > 0:
            characterList.append("at")
            counter = 1  # Indicate "at" has been processed
        else:
            characterList.append("@")
            counter = 1
    else:
        characterList.append(character)

# Combine Characters into a Single String
finalString = ''.join(characterList)

# Ensure Proper End Character
if finalString and finalString[-1] == ".":
    finalString = finalString[:-1] + "dot"

# Output the Final Result
print(finalString)

# End Program
