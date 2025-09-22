# Read input from the user and strip leading/trailing whitespace
input_string = input().strip()

# Replace the terms "dot" with "." and "at" with "@" in the input string
modified_string = input_string.replace("dot", ".").replace("at", "@")

# Handle case where the modified string starts with "."
if modified_string.startswith("."):
    modified_string = "dot" + modified_string[1:]

# Initialize counter for "at" symbols and create an empty list for output
countAt = 0
outputList = []

# Check if the modified string starts with "@", if so, change the first character to "at"
if modified_string.startswith("@"):
    outputList.append("at")
    modified_string = modified_string[1:]

# Process each character in the modified string
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

# Join all characters in outputList to form the final string
final_string = ''.join(outputList)

# If the last character of final_string is ".", replace it with "dot"
if final_string.endswith("."):
    final_string = final_string[:-1] + "dot"

# Print the final modified string
print(final_string)
