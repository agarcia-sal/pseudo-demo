# Step 1: Read Input
input_text = input().strip()

# Step 2: Replace Substrings
modified_text = input_text.replace("dot", ".").replace("at", "@")

# Step 3: Adjust Beginning Character
if modified_text.startswith('.'):
    modified_text = "dot" + modified_text[1:]

# Step 4: Initialize Variables
at_counter = 0
final_output = []
text_length = len(modified_text)

# Step 5: Handle Leading '@'
if modified_text.startswith('@'):
    modified_text = "at" + modified_text[1:]

# Step 6: Iterate Over Each Character
for char in modified_text:
    if char == '@':
        if at_counter > 0:
            final_output.append("at")
        else:
            final_output.append(char)
            at_counter += 1
    else:
        final_output.append(char)

# Step 7: Join Characters
result_string = ''.join(final_output)

# Step 8: Final Adjustment
if result_string.endswith('.'):
    result_string = result_string[:-1] + "dot"

# Step 9: Output Result
print(result_string)
