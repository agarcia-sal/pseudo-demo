# Step 1: Receive Input
input_string = input().strip()

# Step 2: Replace Text Representations
input_string = input_string.replace("dot", ".")
input_string = input_string.replace("at", "@")

# Step 3: Check and Adjust Starting Character
if input_string and input_string[0] == ".":
    input_string = "dot" + input_string

# Step 4: Initialize Variables
count = 0
characters = []

# Step 5: Check for '@' Symbol at Start
if input_string and input_string[0] == "@":
    characters.append("at")
    count = 1

# Step 6: Process Each Character in the String
for currentCharacter in input_string:
    if currentCharacter == "@":
        if count > 0:
            characters.append("at")
            count = 1
        else:
            characters.append("@")
            count = 1
    else:
        characters.append(currentCharacter)

# Step 7: Join Processed Characters
finalString = ''.join(characters)

# Step 8: Handle Trailing Periods
if finalString and finalString[-1] == ".":
    finalString = finalString[:-1] + "dot"

# Step 9: Output the Final String
print(finalString)
