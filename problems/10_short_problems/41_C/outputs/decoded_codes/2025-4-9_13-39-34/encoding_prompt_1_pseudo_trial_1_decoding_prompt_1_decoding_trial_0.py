# Start Program

# Read Input
input_string = input().strip()  # Get a string of characters from the user and remove any leading/trailing whitespace.

# Replace Words with Symbols
input_string = input_string.replace("dot", ".")
input_string = input_string.replace("at", "@")

# Check Start of String
if input_string.startswith("."):
    input_string = "dot" + input_string[1:]  # Prepend "dot" removing the first character.

# Initialize Variables
counter = 0  # Counter for occurrences of "@"
processed_characters = []  # List to store processed characters
length = 0  # Length variable (not used further in pseudocode)

# Check Start of String Again
if input_string.startswith("@"):
    input_string = "at" + input_string[1:]  # Prepend "at" removing the first character.

# Process Each Character
for character in input_string:
    if character == "@":
        if counter > 0:  # Another "@" has already been processed
            processed_characters.append("at")
            counter = 1
        else:
            processed_characters.append("@")
            counter = 1
    else:
        processed_characters.append(character)

# Join Processed Characters
result_string = ''.join(processed_characters)  # Combine all elements in the list into a single string.

# Check End of String
if result_string.endswith("."):
    result_string = result_string[:-1] + "dot"  # Replace the "." at the end with "dot".

# Output the Result
print(result_string)  # Print the final formatted string.

# End Program
