# Function to convert a given input string containing dots into a new encoded string
def encode_string():
    # Read the input string from the user
    input_string = input()
    
    # Initialize variables
    index = 0
    output_string = ""  # Initialize with an empty string

    # Loop through the input string until we reach the end
    while index < len(input_string):
        if input_string[index] == '.':
            # If current character is a '.', add '0' to output_string
            output_string += '0'  # Append '0'
            index += 1  # Move to the next character
        elif index + 1 < len(input_string) and input_string[index + 1] == '.':
            # If next character is also '.', add '1' to output_string
            output_string += '1'  # Append '1'
            index += 2  # Move forward by 2 characters
        else:
            # Otherwise, add '2' to output_string
            output_string += '2'  # Append '2'
            index += 2  # Move forward by 2 characters
    
    # Output the result
    print(output_string)

# You can test the function with different inputs by calling encode_string()
