def process_input():
    # Read input from standard input and strip extra spaces
    input_string = input().strip()

    # Initialize index and result variables
    index = 0
    result = ""

    # Loop until the end of the input string
    while index < len(input_string):
        # Check for the character at the current index
        if input_string[index] == '.':
            result += '0'
            index += 1
        elif index + 1 < len(input_string) and input_string[index + 1] == '.':
            result += '1'
            index += 2
        else:
            result += '2'
            index += 2

    # Print the final result
    print(result)

# Call the function to execute
process_input()
