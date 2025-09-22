# Get the input string from the user
input_string = input()

# Initialize the index counter
index_counter = 0

# Create an empty string to store the decoded output
decoded_output = ""

# Process the input string
while index_counter < len(input_string):
    # Check if the current character is a dot
    if input_string[index_counter] == '.':
        decoded_output += '0'  # Append '0' to the decoded output
        index_counter += 1      # Move to the next character
    # Check if the next character is also a dot
    elif index_counter + 1 < len(input_string) and input_string[index_counter + 1] == '.':
        decoded_output += '1'  # Append '1' to the decoded output
        index_counter += 2      # Skip to the character after next
    else:  # If the current character is a hyphen
        decoded_output += '2'  # Append '2' to the decoded output
        index_counter += 2      # Skip to the character after next

# Output the result
print(decoded_output)
