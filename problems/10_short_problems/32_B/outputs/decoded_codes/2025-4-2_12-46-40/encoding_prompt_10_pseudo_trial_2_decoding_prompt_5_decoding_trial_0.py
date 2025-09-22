# Function to encode a given string based on specific character conditions
def encode_string():
    # Read a line of input and remove any surrounding whitespace
    input_string = input().strip()
    
    # Initialize index and answer variable
    index = 0
    answer = ''
    
    # Loop through characters in the string until the end is reached
    while index < len(input_string):
        # Check the current character for encoding
        if input_string[index] == '.':
            # If it's a single dot, append '0' to the answer
            answer += '0'
            index += 1  # Move to the next character
        elif index + 1 < len(input_string) and input_string[index + 1] == '.':
            # If next character is a dot, append '1' to the answer
            answer += '1'
            index += 2  # Move past the current and next character
        else:
            # In all other cases, append '2' to the answer
            answer += '2'
            index += 2  # Move past the current and next character
    
    # Output the final result
    print(answer)

# Example test case:
# For input '...a..b', the output should be '0212'
