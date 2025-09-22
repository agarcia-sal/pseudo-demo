def convert_string_to_numerical_representation():
    # Step 1: Receive Input
    input_string = input().strip()  # Remove surrounding whitespace

    # Step 2: Initialize Variables
    index = 0
    output_string = ""

    # Step 3: Process the Input String
    while index < len(input_string):
        if input_string[index] == '.':
            # Append '0' if a single dot is encountered
            output_string += '0'
            index += 1  # Move to the next character
        elif index + 1 < len(input_string) and input_string[index + 1] == '.':
            # Append '1' if a pair of dots is found
            output_string += '1'
            index += 2  # Skip the next character
        else:
            # Append '2' for all other characters
            output_string += '2'
            index += 2  # Skip to the character after the next

    # Step 4: Output the Result
    print(output_string)

# Call the function to execute the conversion
convert_string_to_numerical_representation()
