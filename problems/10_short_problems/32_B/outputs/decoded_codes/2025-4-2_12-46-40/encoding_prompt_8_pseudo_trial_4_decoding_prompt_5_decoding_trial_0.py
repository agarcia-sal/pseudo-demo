# Function to translate an encoded string with dots and dashes into a numerical string
def translate_encoding():
    # Read input and remove any extra spaces or newline characters
    encoded_string = input().strip()
    
    # Initialize the current position index and result string
    current_position = 0
    result = ""

    # Process the input string
    while current_position < len(encoded_string):
        if encoded_string[current_position] == '.':
            # If the character is a dot, add '0' to the result
            result += '0'
            current_position += 1  # Move one step forward
        else:
            # Check the next character
            if (current_position + 1 < len(encoded_string) and 
                encoded_string[current_position + 1] == '.'):
                # If the next character is also a dot, add '1' to the result
                result += '1'
                current_position += 2  # Move forward by two steps
            else:
                # Otherwise, add '2' to the result
                result += '2'
                current_position += 2  # Move forward by two steps

    # Output the result string
    print(result)

# Example usage
# translate_encoding()
