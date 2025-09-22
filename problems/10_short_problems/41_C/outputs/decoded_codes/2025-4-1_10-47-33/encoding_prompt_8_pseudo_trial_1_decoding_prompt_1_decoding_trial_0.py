# 1. Read Input 
input_string = input().strip()

# 2. Replace Terms
input_string = input_string.replace("dot", ".")
input_string = input_string.replace("at", "@")

# 3. Handle Leading Character
if input_string.startswith("."):
    input_string = "dot" + input_string[1:]

# 4. Initialize Variables
countAt = 0
outputList = []

# 5. Check Leading Character for "at"
if input_string.startswith("@"):
    input_string = "at" + input_string[1:]

# 6. Process Each Character
for char in input_string:
    if char == "@":
        if countAt > 0:
            outputList.append("at")
            countAt = 1  # to track that we've processed one at least
        else:
            outputList.append("@")
            countAt = 1
    else:
        outputList.append(char)

# 7. Join and Finalize Output
finalString = ''.join(outputList)
if finalString.endswith("."):
    finalString = finalString[:-1] + "dot"

# 8. Print Output
print(finalString)
