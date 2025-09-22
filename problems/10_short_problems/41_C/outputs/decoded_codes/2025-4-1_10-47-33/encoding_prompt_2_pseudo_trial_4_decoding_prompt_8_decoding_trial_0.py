# Step 1: Read input string
input_string = input()

# Step 2: Remove leading or trailing spaces
input_string = input_string.strip()

# Step 3: Replace "dot" with "."
input_string = input_string.replace("dot", ".")

# Step 4: Replace "at" with "@"
input_string = input_string.replace("at", "@")

# Step 5: Check if the first character is a period
if input_string.startswith('.'):
    input_string = 'dot' + input_string

# Step 6: Initialize counter and character list
at_counter = 0
char_list = []

# Step 7: Variable for string length (unused in further code)
string_length = len(input_string)

# Step 8: Check if first character is "@"
if input_string.startswith('@'):
    input_string = 'at' + input_string[1:]

# Step 9: Process each character in modified string
for char in input_string:
    if char == '@':
        if at_counter > 0:
            char_list.append('at')
        else:
            char_list.append('@')
            at_counter += 1
    else:
        char_list.append(char)

# Step 10: Join characters into final result
final_result = ''.join(char_list)

# Step 11: Check if last character is a period
if final_result.endswith('.'):
    final_result = final_result[:-1] + 'dot'

# Step 12: Output the final modified string
print(final_result)
