# Step 1: Read a line of input
input_string = input()

# Step 2: Remove leading and trailing spaces
input_string = input_string.strip()

# Step 3: Replace all occurrences of "dot" with "."
input_string = input_string.replace("dot", ".")

# Step 4: Replace all occurrences of "at" with "@"
input_string = input_string.replace("at", "@")

# Step 5: Check if the first character is a "."
if input_string.startswith("."):
    input_string = "dot" + input_string

# Step 6: Initialize a counter for occurrences of "@"
at_counter = 0
# Create an empty list to store characters
char_list = []

# Step 7: Initialize a variable to track the length of the string (not actively used)
string_length = len(input_string)

# Step 8: Check if the first character is "@"
if input_string.startswith("@"):
    input_string = "at" + input_string[1:]

# Step 9: For each character in the modified string
for char in input_string:
    if char == "@":
        if at_counter > 0:
            char_list.append("at")
        else:
            char_list.append("@")
            at_counter += 1
    else:
        char_list.append(char)

# Step 10: Join all characters in the list into a single string
final_string = ''.join(char_list)

# Step 11: Check if the last character is a "."
if final_string.endswith("."):
    final_string = final_string[:-1] + "dot"

# Step 12: Output the final modified string
print(final_string)
