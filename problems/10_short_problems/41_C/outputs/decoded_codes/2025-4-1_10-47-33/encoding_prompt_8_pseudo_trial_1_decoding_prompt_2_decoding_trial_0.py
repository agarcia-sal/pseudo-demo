# 1. Read Input
input_string = input().strip()

# 2. Replace Terms
modified_string = input_string.replace("dot", ".").replace("at", "@")

# 3. Handle Leading Character
if modified_string and modified_string[0] == ".":
    modified_string = "dot" + modified_string[1:]

# 4. Initialize Variables
countAt = 0
outputList = []

# 5. Check Leading Character for "at"
if modified_string and modified_string[0] == "@":
    modified_string = "at" + modified_string[1:]

# 6. Process Each Character
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

# 7. Join and Finalize Output
finalString = ''.join(outputList)

# Adjust the last character if necessary
if finalString and finalString[-1] == ".":
    finalString = finalString[:-1] + "dot"

# 8. Print Output
print(finalString)
