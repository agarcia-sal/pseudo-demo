def process_dots(input_string):
    # Trim whitespace from the input string
    input_string = input_string.strip()
    
    index = 0
    result_string = ''

    # Loop through the characters in the input string
    while index < len(input_string):
        if input_string[index] == '.':
            # If current character is a dot, append '0'
            result_string += '0'
            index += 1
        elif index + 1 < len(input_string) and input_string[index + 1] == '.':
            # If next character is a dot, append '1'
            result_string += '1'
            index += 2
        else:
            # If the next character is not a dot, append '2'
            result_string += '2'
            index += 2
            
    return result_string

# Read input from the user
input_string = input()
# Process the input and print the result
output = process_dots(input_string)
print(output)
