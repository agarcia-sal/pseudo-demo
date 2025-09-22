# Read Input
emailInput = input().strip()

# Replace Specific Patterns
emailInput = emailInput.replace("dot", ".").replace("at", "@")

# Handling Leading Characters
if emailInput.startswith("."):
    emailInput = "dot" + emailInput[1:]

# Initialize Variables
specialCharacterCount = 0
formattedEmail = []

# Handling Specific Character Structures
if emailInput.startswith("@"):
    emailInput = "at" + emailInput[1:]

# Process Each Character
for char in emailInput:
    if char == "@":
        if specialCharacterCount > 0:
            formattedEmail.append("at")
        else:
            formattedEmail.append("@")
        specialCharacterCount = 1
    else:
        formattedEmail.append(char)

# Construct Final Output
finalEmail = ''.join(formattedEmail)
if finalEmail.endswith("."):
    finalEmail = finalEmail[:-1] + "dot"

# Print Result
print(finalEmail)
