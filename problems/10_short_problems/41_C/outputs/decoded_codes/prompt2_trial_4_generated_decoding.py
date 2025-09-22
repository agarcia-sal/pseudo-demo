# Step 1: Read a line of input from the user
input_string = input()

# Step 2: Remove leading/trailing whitespace
input_string = input_string.strip()

# Step 3: Replace occurrences of "dot" with "."
input_string = input_string.replace("dot", ".")

# Step 4: Replace occurrences of "at" with "@"
input_string = input_string.replace("at", "@")

# Step 5: Check if the first character is a dot
if input_string.startswith('.'):
    input_string = 'dot' + input_string[1:]

# Step 6: Initialize a counter for occurrences of "@" and a list for processed characters
at_counter = 0
processed_chars = []

# Step 7: Initialize variable to track the length of the string
length_of_string = len(input_string)  # This variable may not be used later

# Step 8: Check if the first character is an "@"
if input_string.startswith('@'):
    input_string = 'at' + input_string[1:]

# Step 9: Loop through each character in the modified string
for char in input_string:
    if char == '@':
        if at_counter > 0:  # If this is not the first "@" that has been encountered
            processed_chars.append("at")
        else:
            processed_chars.append("@")
        at_counter += 1
    else:
        processed_chars.append(char)

# Step 10: Join characters into a single output string
final_string = ''.join(processed_chars)

# Step 11: Check if the last character is a dot
if final_string.endswith('.'):
    final_string = final_string[:-1] + "dot"

# Step 12: Output the final processed string
print(final_string)
