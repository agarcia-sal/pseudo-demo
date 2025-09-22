def process_input_string():
    # Step 1: Read input string and remove extra spaces
    input_string = input().strip() 

    # Step 2: Initialize variables
    current_position = 0
    result = ""

    # Step 3: Process the input string
    while current_position < len(input_string):
        if input_string[current_position] == '.':
            # If the current character is a dot
            result += '0'
            current_position += 1
        elif current_position + 1 < len(input_string) and input_string[current_position + 1] == '.':
            # If the next character is also a dot
            result += '1'
            current_position += 2
        else:
            # Any other character or situation
            result += '2'
            current_position += 2

    # Step 4: Output the result
    print(result)

# Call the function to execute
process_input_string()
