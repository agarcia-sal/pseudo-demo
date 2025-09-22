# 1. Read Input:
user_input = input().strip()

# 2. Replace Keywords:
modified_string = user_input.replace("dot", ".").replace("at", "@")

# 3. Check for Leading Dot:
if modified_string.startswith("."):
    modified_string = "dot" + modified_string

# 4. Initialize Variables:
co = 0  # counter for '@' appearances
c = []  # list to store processed characters
l = 0   # unused variable

# 5. Fix the Leading At:
if modified_string.startswith("@"):
    modified_string = "at" + modified_string

# 6. Process Each Character:
for char in modified_string:
    if char == "@":
        if co > 0:
            c.append("at")
        else:
            c.append("@")
            co = 1  # set counter to 1
    else:
        c.append(char)  # append the character to the list

# 7. Combine Characters:
final_string = ''.join(c)

# 8. Adjust Trailing Dot:
if final_string.endswith("."):
    final_string = final_string[:-1] + "dot"

# 9. Output the Result:
print(final_string)
