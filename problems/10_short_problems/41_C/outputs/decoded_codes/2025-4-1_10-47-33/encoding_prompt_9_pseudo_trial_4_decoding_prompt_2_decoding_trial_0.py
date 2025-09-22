# 1. Receive Input
input_string = input().strip()

# 2. Replace Keywords
modified_string = input_string.replace("dot", ".").replace("at", "@")

# 3. Check Leading Character
if modified_string.startswith("."):
    modified_string = "dot" + modified_string[1:]

# 4. Initialize the List and Counter
counter = 0
processed_chars = []

# 5. Check for Leading "at"
if modified_string.startswith("@"):
    modified_string = "at" + modified_string[1:]

# 6. Process Each Character
for char in modified_string:
    if char == "@":
        if counter > 0:
            processed_chars.append("at")
            counter = 1
        else:
            processed_chars.append("@")
            counter = 1
    else:
        processed_chars.append(char)

# 7. Reconstruct the String
final_string = ''.join(processed_chars)

# 8. Check for Trailing Character
if final_string.endswith("."):
    final_string = final_string[:-1] + "dot"

# 9. Output the Result
print(final_string)
