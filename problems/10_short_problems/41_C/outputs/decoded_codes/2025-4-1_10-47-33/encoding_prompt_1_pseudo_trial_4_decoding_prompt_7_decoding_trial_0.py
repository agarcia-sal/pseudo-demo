# Begin program

# Step 1: Read input string and trim whitespace
input_string = input().strip()

# Step 2: Replace occurrences of "dot" with "."
modified_string = input_string.replace("dot", ".")

# Step 3: Replace occurrences of "at" with "@"
modified_string = modified_string.replace("at", "@")

# Step 4: Check if the first character is "."
if modified_string and modified_string[0] == ".":
    modified_string = "dot" + modified_string[1:]  # Prepend "dot" excluding the first character

# Step 5: Initialize a counter for "@" and a list to hold processed characters
co = 0  # Counter for consecutive "@"
c = []  # List to hold processed characters
l = 0   # Not used for further logic

# Step 8: Check if the first character is "@"
if modified_string and modified_string[0] == "@":
    modified_string = "at" + modified_string[1:]  # Prepend "at" excluding the first character

# Step 9: Process each character in the modified string
for i in modified_string:
    if i == "@":  # Check if the current character is "@"
        if co > 0:  # If "@" was seen before
            c.append("at")  # Append "at" to the list
            co = 1  # Set co to 1
        else:
            c.append("@")  # Append "@" to the list
            co = 1  # Set co to 1
    else:
        c.append(i)  # Append the regular character to the list

# Step 10: Join all characters in the list "c" to form the final string
final_string = ''.join(c)

# Step 11: Check if the last character of the final string is "."
if final_string and final_string[-1] == ".":
    final_string = final_string[:-1] + "dot"  # Replace the last character with "dot"

# Step 12: Print the final processed string
print(final_string)

# End program
