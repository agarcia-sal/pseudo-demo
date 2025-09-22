# Step 1: Read Input
input_text = input().strip()

# Step 2: Replace Keywords
modified_text = input_text.replace("dot", ".").replace("at", "@")

# Step 3: Check for Leading Dot
if modified_text.startswith("."):
    modified_text = "dot" + modified_text

# Step 4: Initialize Variables
co = 0
c = []

# Step 5: Fix the Leading At
if modified_text.startswith("@"):
    modified_text = "at" + modified_text

# Step 6: Process Each Character
for char in modified_text:
    if char == "@":
        if co > 0:
            c.append("at")
        else:
            c.append("@")
        co = 1
    else:
        c.append(char)
        co = 0

# Step 7: Combine Characters
result = ''.join(c)

# Step 8: Adjust Trailing Dot
if result.endswith("."):
    result = result[:-1] + "dot"

# Step 9: Output the Result
print(result)
