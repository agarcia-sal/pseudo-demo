# Read Input
input_string = input().strip()

# Replace Terms
modified_string = input_string.replace("dot", ".").replace("at", "@")

# Handle Leading Character
if modified_string.startswith("."):
    modified_string = "dot" + modified_string[1:]

# Initialize Variables
countAt = 0
outputList = []

# Check Leading Character for "at"
if modified_string.startswith("@"):
    modified_string = "at" + modified_string[1:]

# Process Each Character
for char in modified_string:
    if char == "@":
        if countAt > 0:
            outputList.append("at")
            countAt = 1
        else:
            outputList.append("@")
            countAt = 1
    else:
        outputList.append(char)

# Join and Finalize Output
finalString = ''.join(outputList)
if finalString.endswith("."):
    finalString = finalString[:-1] + "dot"

# Print Output
print(finalString)
