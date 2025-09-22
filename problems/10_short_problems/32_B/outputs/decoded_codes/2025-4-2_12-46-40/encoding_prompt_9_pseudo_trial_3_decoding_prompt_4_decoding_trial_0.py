def convert_signal_to_number():
    # Step 1: Initialize Input
    input_string = input().strip()  # Read input and remove extra spaces

    # Step 2: Setup Variables
    index = 0
    output_string = ""

    # Step 3: Process Input String
    while index < len(input_string):
        if input_string[index] == '.':
            output_string += '0'
            index += 1
        elif index + 1 < len(input_string) and input_string[index + 1] == '.':
            output_string += '1'
            index += 2
        else:
            output_string += '2'
            index += 2

    # Step 4: Output Result
    print(output_string)

# Call the function to execute the conversion
convert_signal_to_number()
