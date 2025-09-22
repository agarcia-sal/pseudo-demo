# 1. Receive Input
input_string = input().strip()

# 2. Replace Keywords
modified_string = input_string.replace("dot", ".").replace("at", "@")

# 3. Check for Leading Symbols
if modified_string.startswith("."):
    modified_string = "dot" + modified_string

# 4. Initialize Variables
at_counter = 0
char_list = []
length = 0

# 5. Check for Leading "at"
if modified_string.startswith("@"):
    modified_string = "at" + modified_string

# 6. Process Each Character
for char in modified_string:
    if char == "@":
        if at_counter > 0:
            char_list.append("at")
            at_counter = 1
        else:
            char_list.append("@")
            at_counter = 1
    else:
        char_list.append(char)

# 7. Join Characters
final_string = ''.join(char_list)

# 8. Check Trailing Symbols
if final_string.endswith("."):
    final_string = final_string[:-1] + "dot"

# 9. Output the Result
print(final_string)
