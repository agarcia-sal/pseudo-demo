# Function to decode a sequence of characters into a numerical representation
def decode_string():
    # Accept a string of characters from the user
    input_string = input()
    
    # Initialize variables
    index = 0  # Index counter to track position in input string
    decoded_output = ""  # String to store the result of the decoding process

    # Process the input string
    while index < len(input_string):
        if input_string[index] == '.':
            decoded_output += '0'  # Append '0' for current dot
            index += 1  # Move to the next character
        elif index + 1 < len(input_string) and input_string[index + 1] == '.':
            decoded_output += '1'  # Append '1' for two consecutive dots
            index += 2  # Skip to the character after next
        else:  # Current character is a hyphen
            decoded_output += '2'  # Append '2' for the hyphen
            index += 2  # Skip to the character after next

    # Output the result
    print(decoded_output)

# Sample test cases (uncomment to test)
# Input: '..--.'
# Expected Output: '0012'
# decode_string()
# Input: '...--..'
# Expected Output: '0012'
# decode_string()
