# 1. Receive Input:
input_string = input().strip()

# 2. Replace Text Representations:
input_string = input_string.replace("dot", ".")
input_string = input_string.replace("at", "@")

# 3. Check and Adjust Starting Character:
if input_string and input_string[0] == ".":
    input_string = "dot" + input_string

# 4. Initialize Variables:
count = 0
characters = []

# 5. Check for '@' Symbol at Start:
if input_string and input_string[0] == "@":
    input_string = "at" + input_string

# 6. Process Each Character in the String:
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

# 7. Join Processed Characters:
finalString = ''.join(characters)

# 8. Handle Trailing Periods:
if finalString and finalString[-1] == ".":
    finalString = finalString[:-1] + "dot"

# 9. Output the Final String:
print(finalString)
