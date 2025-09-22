# 1. Read Input
text = input().strip()

# 2. Replace Substrings
text = text.replace("dot", ".")
text = text.replace("at", "@")

# 3. Adjust Beginning Character
if text.startswith("."):
    text = "dot" + text[1:]

# 4. Initialize Variables
at_counter = 0
final_characters = []
length_of_text = len(text)

# 5. Handle Leading '@'
if text.startswith("@"):
    text = "at" + text[1:]

# 6. Iterate Over Each Character
for char in text:
    if char == '@':
        if at_counter > 0:  # This is not the first '@' found
            final_characters.append("at")
        else: 
            final_characters.append(char)
        at_counter += 1
    else:
        final_characters.append(char)

# 7. Join Characters
result = ''.join(final_characters)

# 8. Final Adjustment
if result.endswith("."):
    result = result[:-1] + "dot"

# 9. Output Result
print(result)
