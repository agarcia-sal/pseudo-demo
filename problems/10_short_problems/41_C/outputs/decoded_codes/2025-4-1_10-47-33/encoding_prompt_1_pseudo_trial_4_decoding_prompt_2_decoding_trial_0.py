# Begin program

# Step 1: Read input string and remove leading or trailing whitespace
input_string = input().strip()

# Step 2: Replace "dot" with "."
modified_string = input_string.replace("dot", ".")

# Step 3: Replace "at" with "@"
modified_string = modified_string.replace("at", "@")

# Step 4: Prepend "dot" if the first character is "."
if modified_string and modified_string[0] == ".":
    modified_string = "dot" + modified_string[1:]

# Step 5: Initialize a counter to track consecutive "@"
co = 0

# Step 6: Initialize an empty list to hold processed characters
c = []

# Step 7: Initialize variable l (not used further)
l = 0

# Step 8: Prepend "at" if the first character is "@"
if modified_string and modified_string[0] == "@":
    modified_string = "at" + modified_string[1:]

# Step 9: Process each character in the modified string
for i in modified_string:
    # Step 9a: Check if character is "@"
    if i == "@":
        # Step 9a.i: Check if we have seen "@" already
        if co > 0:
            c.append("at")
            co = 1
        else:
            c.append("@")
            co = 1
    else:
        # Step 9b: Append the character to list c
        c.append(i)
        co = 0  # Reset co since this is not "@" 

# Step 10: Join characters in list c into a single string
final_string = ''.join(c)

# Step 11: Replace last character with "dot" if it is "."
if final_string and final_string[-1] == ".":
    final_string = final_string[:-1] + "dot"

# Step 12: Print the final processed string
print(final_string)

# End program
