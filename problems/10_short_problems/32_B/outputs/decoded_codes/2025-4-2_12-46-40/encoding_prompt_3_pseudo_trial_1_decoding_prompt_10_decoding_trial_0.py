def process_dots():
    # Read input from standard input and remove any surrounding whitespace
    input_string = input().strip()

    # Initialize an index for tracking the current position in the input string
    index = 0
    
    # Initialize an empty string to store the output result
    result = ""
    
    # While the index is less than the length of the input string
    while index < len(input_string):
        if input_string[index] == '.':
            # Current character is a dot (.)
            result += '0'  # Append '0' to result
            index += 1  # Increment index by 1
        elif index + 1 < len(input_string) and input_string[index + 1] == '.':
            # Next character is also a dot (.)
            result += '1'  # Append '1' to result
            index += 2  # Increment index by 2
        else:
            # Current character is not a dot and the next character is not a dot
            result += '2'  # Append '2' to result
            index += 2  # Increment index by 2

    # Output the final result
    print(result)

# Call the function to execute
process_dots()
