# Initialize the function to process input
def process_input():
    # Read input from standard input and remove leading/trailing whitespace
    input_string = input().strip()
    
    # Initialize index and result variable
    index = 0
    result = ""

    # Process each character in the input string
    while index < len(input_string):
        # Check if the current character is a period
        if input_string[index] == '.':
            # Append '0' to the result
            result += '0'
            # Move the index to the next character
            index += 1
        else:
            # Check the next character if we are not at the end of the string
            if index + 1 < len(input_string):
                # Check if the next character is a period
                if input_string[index + 1] == '.':
                    # Append '1' to the result
                    result += '1'
                    # Move the index forward by 2
                    index += 2
                else:
                    # If neither character is a period, append '2' to the result
                    result += '2'
                    # Move the index forward by 2
                    index += 2
            else:
                # If there's no next character, consider this scenario
                result += '2'
                index += 1

    # Output the final result
    print(result)

# Call the function to execute the processing
process_input()
