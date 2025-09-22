# Read Input
input_string = input().strip()

# Replace Specific Words
input_string = input_string.replace("dot", ".").replace("at", "@")

# Handle Leading Period
if input_string.startswith("."):
    input_string = "dot" + input_string[1:]

# Initialize Variables
at_counter = 0
result_chars = []

# Handle Leading At-Symbol
if input_string.startswith("@"):
    input_string = "at" + input_string[1:]

# Process Each Character
for char in input_string:
    if char == "@":
        if at_counter > 0:
            result_chars.append("at")
            at_counter = 1
        else:
            result_chars.append("@")
            at_counter = 1
    else:
        result_chars.append(char)

# Join Characters Together
result_string = ''.join(result_chars)

# Handle Trailing Period
if result_string.endswith("."):
    result_string = result_string[:-1] + "dot"

# Output the Result
print(result_string)
