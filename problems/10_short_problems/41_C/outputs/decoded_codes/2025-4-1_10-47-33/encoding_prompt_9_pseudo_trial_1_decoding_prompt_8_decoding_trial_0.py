# Step 1: Receive Input
input_string = input().strip()

# Step 2: Replace Word Aliases
modified_string = input_string.replace("dot", ".").replace("at", "@")

# Step 3: Adjust Beginning of String
if modified_string.startswith("."):
    modified_string = "dot" + modified_string

# Step 4: Initialize Counters
at_counter = 0
char_list = []

# Step 5: Handle Special Cases for Starting Character
if modified_string.startswith("@"):
    modified_string = "at" + modified_string[1:]

# Step 6: Iterate through Each Character
for char in modified_string:
    if char == "@":
        if at_counter > 0:
            char_list.append("at")
            at_counter = 1
        else:
            char_list.append("@")
            at_counter += 1
    else:
        char_list.append(char)

# Step 7: Combine List into String
result_string = ''.join(char_list)

# Step 8: Adjust End of String
if result_string.endswith("."):
    result_string = result_string[:-1] + "dot"

# Step 9: Output Modified String
print(result_string)


replacement_mapping = {
    "dot": ".",
    "at": "@",
    # Add more mappings as necessary
}

for word, replacement in replacement_mapping.items():
    modified_string = modified_string.replace(word, replacement)
