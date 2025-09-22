# Start of the program
# Read input from the user and remove surrounding whitespace
input_string = input().strip()

# Replace specific terms in the string
input_string = input_string.replace("dot", ".")
input_string = input_string.replace("at", "@")

# Prepend "dot" if the string starts with a "."
if input_string.startswith("."):
    input_string = "dot" + input_string[1:]

# Initialize a counter and an empty list for processed characters
at_counter = 0
processed_characters = []

# Ensure "at" handling if the string starts with "@"
if input_string.startswith("@"):
    input_string = "at" + input_string[1:]

# Process each character in the string
for character in input_string:
    if character == "@":
        if at_counter > 0:
            processed_characters.append("at")  # Replace subsequent "@" with "at"
        else:
            processed_characters.append("@")  # First "@" remains as "@" 
        at_counter += 1  # Increment the counter for each "@" encountered
    else:
        processed_characters.append(character)  # Add other characters unchanged

# Combine the list into a single string
final_string = "".join(processed_characters)

# Final adjustment for string ending
if final_string.endswith("."):
    final_string = final_string[:-1] + "dot"  # Replace ending "." with "dot"

# Output the final result
print(final_string)
