# Start Program

# Read Input
input_string = input().strip()  # Get a string of characters and remove any leading/trailing whitespace.

# Replace Words with Symbols
input_string = input_string.replace("dot", ".")  # Replace every occurrence of "dot" with "."
input_string = input_string.replace("at", "@")    # Replace every occurrence of "at" with "@"

# Check Start of String
if input_string.startswith("."):  # If the first character is "."
    input_string = "dot" + input_string[1:]  # Prepend "dot" and remove the first character

# Initialize Variables
counter = 0  # Counter to track occurrences of "@"
result_list = []  # List to store processed characters
length = 0  # Length variable (not used in the logic, but initialized)

# Check Start of String Again
if input_string.startswith("@"):  # If the first character is "@"
    input_string = "at" + input_string[1:]  # Prepend "at" and remove the first character

# Process Each Character
for char in input_string:
    if char == "@":  # If the character is "@"
        if counter > 0:  # If another "@" has already been processed
            result_list.append("at")  # Append "at" to the list
            counter = 1  # Set counter to one
        else:
            result_list.append("@")  # Append "@" to the list
            counter = 1  # Set counter to one
    else:  # If the character is not "@"
        result_list.append(char)  # Append the character to the list

# Join Processed Characters
final_result = ''.join(result_list)  # Combine all elements in the list into a single string.

# Check End of String
if final_result.endswith("."):  # If the last character is "."
    final_result = final_result[:-1] + "dot"  # Replace "." at the end with "dot"

# Output the Result
print(final_result)  # Print the final formatted string.

# End Program
