def process_input():
    # Read input from standard input and remove leading/trailing whitespace
    input_string = input().strip()
    
    # Initialize index variable and result string
    index = 0
    result_string = ''

    # Loop through the characters in input_string until the end is reached
    while index < len(input_string):
        # Check if the current character is a dot
        if input_string[index] == '.':
            result_string += '0'
            index += 1
        # Check if the next character is a dot
        elif index + 1 < len(input_string) and input_string[index + 1] == '.':
            result_string += '1'
            index += 2
        # If neither condition is met
        else:
            result_string += '2'
            index += 2

    # Output the result string
    print(result_string)

# Run the process_input function
process_input()
