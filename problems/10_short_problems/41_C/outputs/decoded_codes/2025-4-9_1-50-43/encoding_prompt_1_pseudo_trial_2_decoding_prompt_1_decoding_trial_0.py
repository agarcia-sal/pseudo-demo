# Step 1: Read Input
user_input = input().strip()

# Step 2: Substitute Specific Words
user_input = user_input.replace("dot", ".").replace("at", "@")

# Step 3: Check Beginning of String
if user_input.startswith("."):
    user_input = "dot" + user_input[1:]

# Step 4: Initialize Variables
co = 0  # counter for occurrences of "@"
c = []  # empty list to hold characters
l = 0   # not used, but initialized

# Step 5: Check Beginning for '@' Symbol
if user_input.startswith("@"):
    user_input = "at" + user_input[1:]

# Step 6: Build New String
for i in user_input:
    if i == "@":
        if co > 0:  # If more than one "@" symbol found
            c.append("at")
            co = 1
        else:
            c.append("@")
            co = 1
    else:
        c.append(i)

# Step 7: Join List into String
final_string = ''.join(c)

# Step 8: Check End of String
if final_string.endswith("."):
    final_string = final_string[:-1] + "dot"

# Step 9: Output Result
print(final_string)
