# Step 1: Receive Input
email_string = input().strip()

# Step 2: Replace Word Aliases
email_string = email_string.replace("dot", ".")
email_string = email_string.replace("at", "@")

# Step 3: Adjust Beginning of String
if email_string.startswith("."):
    email_string = "dot" + email_string

# Step 4: Initialize Counters
counter = 0
char_list = []

# Step 5: Handle Special Cases for Starting Character
if email_string.startswith("@"):
    email_string = "at" + email_string[1:]

# Step 6: Iterate through Each Character
for char in email_string:
    if char == "@":
        if counter > 0:
            char_list.append("at")
            counter = 1
        else:
            char_list.append("@")
            counter = 1
    else:
        char_list.append(char)

# Step 7: Combine List into String
modified_string = ''.join(char_list)

# Step 8: Adjust End of String
if modified_string.endswith("."):
    modified_string = modified_string[:-1] + "dot"

# Step 9: Output Modified String
print(modified_string)
