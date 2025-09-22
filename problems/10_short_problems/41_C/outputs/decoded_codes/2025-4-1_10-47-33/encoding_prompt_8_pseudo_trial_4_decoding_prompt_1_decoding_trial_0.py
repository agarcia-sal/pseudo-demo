# Step 1: Read Input
input_string = input().strip()

# Step 2: Replace Specific Words
input_string = input_string.replace("dot", ".")
input_string = input_string.replace("at", "@")

# Step 3: Handle Leading Period
if input_string.startswith("."):
    input_string = "dot" + input_string[1:]  # Prepend "dot" and remove leading period

# Step 4: Initialize Variables
at_counter = 0
processed_chars = []

# Step 5: Handle Leading At-Symbol
if input_string.startswith("@"):
    input_string = "at" + input_string[1:]  # Replace leading "@" with "at"

# Step 6: Process Each Character
for char in input_string:
    if char == "@":
        if at_counter > 0:
            processed_chars.append("at")  # Replace additional "@" with "at"
            at_counter = 1  # Indicate processed at-symbol
        else:
            processed_chars.append(char)  # Keep the first "@" as is
            at_counter = 1
    else:
        processed_chars.append(char)  # Append other characters

# Step 7: Join Characters Together
result_string = ''.join(processed_chars)

# Step 8: Handle Trailing Period
if result_string.endswith("."):
    result_string = result_string[:-1] + "dot"  # Replace trailing period with "dot"

# Step 9: Output the Result
print(result_string)
