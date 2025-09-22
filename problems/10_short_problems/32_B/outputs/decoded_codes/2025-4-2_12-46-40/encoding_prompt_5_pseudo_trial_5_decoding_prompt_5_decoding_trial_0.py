# Function to decode the input string based on specific rules
def decode_string():
    # Read a single line of input and trim any surrounding spaces
    input_string = input().strip()
    
    # Initialize index to track the current position in the input string
    index = 0
    # Initialize an empty string for the output result
    output_string = ""

    # Process the input string while there are more characters to process
    while index < len(input_string):
        # If the current character is a dot ('.')
        if input_string[index] == '.':
            output_string += '0'  # Append '0'
            index += 1  # Move to the next character
        # If the next character is a dot ('.')
        elif index + 1 < len(input_string) and input_string[index + 1] == '.':
            output_string += '1'  # Append '1'
            index += 2  # Move past this pair of characters
        else:
            output_string += '2'  # Append '2'
            index += 2  # Move past this pair of characters if it's not handled above

    # Output the final decoded string
    print(output_string)

# Uncomment the line below to run the function when executing the script
# decode_string()

# Example test case:
# Input: "... .. ... ."
# Expected output: "0001210"
