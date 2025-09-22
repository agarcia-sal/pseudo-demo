# Function to process the input string and generate the result
def process_input_string(input_string):
    # Initialize index and result string
    index = 0
    result = ''

    # Process each character in the input string
    while index < len(input_string):
        # Check for the first character
        if input_string[index] == '.':
            # If character is '.', append '0' to result
            result += '0'
            # Move to the next character
            index += 1
        # Check the next character if there is one
        elif index + 1 < len(input_string) and input_string[index + 1] == '.':
            # If the next character is also '.', append '1' to result
            result += '1'
            # Move past this pair of characters
            index += 2
        else:
            # If neither condition is met, append '2' to result
            result += '2'
            # Move past this pair of characters
            index += 2

    return result

# Read input string from standard input
input_string = input()
# Process the string and output the result
output_result = process_input_string(input_string)
print(output_result)
