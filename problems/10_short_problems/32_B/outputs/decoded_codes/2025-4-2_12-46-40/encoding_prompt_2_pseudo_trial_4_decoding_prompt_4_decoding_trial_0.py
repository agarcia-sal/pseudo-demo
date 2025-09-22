# Read and trim the input string
input_string = input().strip()

# Initialize variables
current_index = 0
output_string = ""

# Process the input string character by character
while current_index < len(input_string):
    # Check the current character
    if input_string[current_index] == '.':
        output_string += '0'  # Append '0' for single dot
        current_index += 1  # Move to the next character
    else:
        # Check the next character, ensuring we're within bounds
        if current_index + 1 < len(input_string) and input_string[current_index + 1] == '.':
            output_string += '1'  # Append '1' for character followed by dot
            current_index += 2  # Move to the character after the dot
        else:
            output_string += '2'  # Append '2' if the next is not a dot
            current_index += 2  # Move to the character after the next

# Print the transformed output string
print(output_string)
