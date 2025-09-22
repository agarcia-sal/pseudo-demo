# Begin program

# Step 1: Read input string and remove leading/trailing whitespace
input_string = input().strip()

# Step 2: Replace "dot" with "."
modified_string = input_string.replace("dot", ".")

# Step 3: Replace "at" with "@"
modified_string = modified_string.replace("at", "@")

# Step 4: Check if the first character is '.', prepend 'dot' if so
if modified_string and modified_string[0] == ".":
    modified_string = "dot" + modified_string[1:]

# Step 5: Initialize a counter for consecutive '@'
co = 0 

# Step 6: Initialize an empty list to hold processed characters
c = []

# Step 7: Initialize variable 'l' not used further but we'll set it to 0
l = 0 

# Step 8: Check if the first character is '@', prepend 'at' if so
if modified_string and modified_string[0] == "@":
    modified_string = "at" + modified_string[1:]

# Step 9: Process each character in the modified string
for i in modified_string:
    if i == "@":
        if co > 0:  # If '@' has been seen already
            c.append("at")
            co = 1  # Reset to indicate '@' was added
        else:
            c.append("@")
            co = 1  # Update co indicating one '@' has been seen
    else:
        c.append(i)  # Append the regular character to the list
        co = 0  # Reset co if any other character is added

# Step 10: Join the characters in list 'c' into a final string
final_string = ''.join(c)

# Step 11: Check if the last character is '.', replace it with 'dot'
if final_string and final_string[-1] == ".":
    final_string = final_string[:-1] + "dot"

# Step 12: Print the final processed string
print(final_string)

# End program
