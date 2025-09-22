def convert_string_to_numerical():
    # Step 2: Receive Input
    input_string = input().strip()

    # Step 3: Initialize Variables
    current_index = 0
    output_string = ""

    # Step 4: Process Input String
    while current_index < len(input_string):
        # If the current character is a dot
        if input_string[current_index] == '.':
            output_string += '0'
            current_index += 1
        # If the current character is not a dot and the next is a dot
        elif current_index + 1 < len(input_string) and input_string[current_index + 1] == '.':
            output_string += '1'
            current_index += 2
        # If neither condition is met
        else:
            output_string += '2'
            current_index += 2

    # Step 5: Output Result
    print(output_string)

# To execute the function:
convert_string_to_numerical()
