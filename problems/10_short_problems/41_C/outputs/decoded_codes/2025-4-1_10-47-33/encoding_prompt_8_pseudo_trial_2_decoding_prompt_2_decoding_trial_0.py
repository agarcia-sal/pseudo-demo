# Step 1: Read Input
emailString = input().strip()

# Step 2: Replace Keywords
emailString = emailString.replace("dot", ".")
emailString = emailString.replace("at", "@")

# Step 3: Handle Leading Period
if emailString.startswith('.'):
    emailString = "dot" + emailString[1:]

# Step 4: Check for Leading At Symbol
if emailString.startswith('@'):
    emailString = "at" + emailString[1:]

# Step 5: Prepare for Conversion
counter = 0
formattedCharacters = []

# Step 6: Process Each Character
for character in emailString:
    if character == '@':
        if counter > 0:
            formattedCharacters.append("at")
            counter = 1
        else:
            formattedCharacters.append("@")
            counter = 1
    else:
        formattedCharacters.append(character)

# Step 7: Join Characters into a String
finalString = ''.join(formattedCharacters)

# Step 8: Handle Trailing Period
if finalString.endswith('.'):
    finalString = finalString[:-1] + "dot"

# Step 9: Output the Result
print(finalString)
