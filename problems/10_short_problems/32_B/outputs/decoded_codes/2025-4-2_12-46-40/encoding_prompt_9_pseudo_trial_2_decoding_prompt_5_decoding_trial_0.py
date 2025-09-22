# Function to convert a specific string input into a numerical string
def convert_string_to_numbers():
    # Step 2: Receive Input
    input_string = input().strip()  # Read and trim whitespace from input

    # Step 3: Initialize Variables
    current_index = 0  # To track the position in the input string
    output_string = ""  # To store the resulting numerical representation

    # Step 4: Process Input String
    while current_index < len(input_string):  # Loop until the end of the string
        if input_string[current_index] == '.':  # Check for a dot
            output_string += '0'  # Append '0' to the output
            current_index += 1  # Move to the next character
        elif current_index + 1 < len(input_string) and input_string[current_index + 1] == '.':
            output_string += '1'  # Append '1' to the output
            current_index += 2  # Move to the character after the next
        else:
            output_string += '2'  # Append '2' to the output
            current_index += 2  # Move to the character after the next

    # Step 5: Output Result
    print(output_string)  # Print the final numerical representation

# Example usage:
# convert_string_to_numbers()  # Uncomment to run the function
