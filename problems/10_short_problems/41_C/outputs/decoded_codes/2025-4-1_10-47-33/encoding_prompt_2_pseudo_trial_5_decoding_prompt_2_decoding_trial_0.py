# Step 1: Read Input
text = input().strip()

# Step 2: Replace Substrings
text = text.replace("dot", ".")
text = text.replace("at", "@")

# Step 3: Adjust Beginning Character
if text.startswith('.'):
    text = "dot" + text[1:]

# Step 4: Initialize Variables
counter = 0
output_chars = []
length_of_text = 0

# Step 5: Handle Leading '@'
if text.startswith('@'):
    text = "at" + text[1:]

# Step 6: Iterate Over Each Character
for char in text:
    if char == '@':
        if counter > 0:  # Not the first '@'
            output_chars.append("at")
        else:  # First '@'
            output_chars.append('@')
            counter += 1
    else:
        output_chars.append(char)

# Step 7: Join Characters
final_output = ''.join(output_chars)

# Step 8: Final Adjustment
if final_output.endswith('.'):
    final_output = final_output[:-1] + "dot"

# Step 9: Output Result
print(final_output)
