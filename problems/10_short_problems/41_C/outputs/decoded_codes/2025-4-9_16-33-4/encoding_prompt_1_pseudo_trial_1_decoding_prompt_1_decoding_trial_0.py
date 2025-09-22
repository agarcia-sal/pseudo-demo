# Start Program

# Read Input
input_string = input().strip()  # Get a string of characters from the user and remove any leading/trailing whitespace.

# Replace Words with Symbols
input_string = input_string.replace("dot", ".")  # Replace every occurrence of "dot" with "."
input_string = input_string.replace("at", "@")    # Replace every occurrence of "at" with "@"

# Check Start of String
if input_string and input_string[0] == ".":  # Check first character
    input_string = "dot" + input_string[1:]  # Prepend "dot" and remove the first character

# Initialize Variables
counter = 0  # Create a counter variable to track occurrences of "@"
processed_characters = []  # Create an empty list to store processed characters
length = 0  # Set the length variable to zero

# Check Start of String Again
if input_string and input_string[0] == "@":  # Check first character again
    input_string = "at" + input_string[1:]  # Prepend "at" and remove the first character

# Process Each Character
for char in input_string:
    if char == "@":  # If character is "@"
        if counter > 0:  # If another "@" has already been processed
            processed_characters.append("at")
            counter = 1
        else:
            processed_characters.append("@")
            counter = 1
    else:  # If character is not "@"
        processed_characters.append(char)

# Join Processed Characters
result_string = ''.join(processed_characters)  # Combine all elements in the list into a single string

# Check End of String
if result_string and result_string[-1] == ".":  # If last character is "."
    result_string = result_string[:-1] + "dot"  # Replace the "." at the end with "dot"

# Output the Result
print(result_string)  # Print the final formatted string

# End Program
