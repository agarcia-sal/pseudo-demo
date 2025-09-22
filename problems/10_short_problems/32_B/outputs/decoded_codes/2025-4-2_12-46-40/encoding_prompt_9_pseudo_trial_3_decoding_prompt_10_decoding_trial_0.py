def convert_signals_to_numbers():
    # Step 1: Initialize Input
    input_string = input().strip()  # Read input and remove extra spaces

    # Step 2: Setup Variables
    index = 0
    output_string = ""

    # Step 3: Process Input String
    while index < len(input_string):
        if input_string[index] == '.':
            output_string += '0'  # Add '0' to output
            index += 1  # Move to the next character
        elif index + 1 < len(input_string) and input_string[index + 1] == '.':
            output_string += '1'  # Add '1' to output
            index += 2  # Skip the next character
        else:
            output_string += '2'  # Add '2' to output
            index += 2  # Skip the next character

    # Step 4: Output Result
    print(output_string)

# Calling the function to execute the conversion
convert_signals_to_numbers()
