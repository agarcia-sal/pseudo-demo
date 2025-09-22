# Step 1: Read Input
input_text = input().strip()  # Accept a line of text and remove whitespace

# Step 2: Replace Keywords
modified_string = input_text.replace("dot", ".").replace("at", "@")

# Step 3: Check for Leading Dot
if modified_string.startswith("."):
    modified_string = "dot" + modified_string

# Step 4: Initialize Variables
co = 0  # Counter for appearances of "@" 
c = []  # List to store processed characters
l = 0   # This variable seems unused

# Step 5: Fix the Leading At
if modified_string.startswith("@"):
    modified_string = "at" + modified_string

# Step 6: Process Each Character
for char in modified_string:
    if char == "@":
        if co > 0:
            c.append("at")
            co = 1  # Reset counter after appending "at"
        else:
            c.append("@")
            co = 1  # Set counter to 1 when seeing first "@"
    else:
        c.append(char)

# Step 7: Combine Characters
final_string = ''.join(c)

# Step 8: Adjust Trailing Dot
if final_string.endswith("."):
    final_string = final_string[:-1] + "dot"  # Replace trailing dot with "dot"

# Step 9: Output the Result
print(final_string)
