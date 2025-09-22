def process_input_string():
    # Read and clean the input string by removing leading/trailing whitespace
    input_string = input().strip()
    
    # Initialize index and result variable
    index = 0
    result = ""

    # Process each character in the input string
    while index < len(input_string):
        if input_string[index] == '.':
            # If the current character is a period, append '0' and move to the next character
            result += '0'
            index += 1
        else:
            # Check if there is a next character to look at
            if index + 1 < len(input_string):
                if input_string[index + 1] == '.':
                    # If the next character is a period, append '1' and move forward by 2
                    result += '1'
                    index += 2
                else:
                    # If neither character is a period, append '2' and move forward by 2
                    result += '2'
                    index += 2
            else:
                # If there's no next character, simply append '2'
                result += '2'
                index += 1

    # Output the final result
    print(result)


# Call the function to execute the code
process_input_string()
