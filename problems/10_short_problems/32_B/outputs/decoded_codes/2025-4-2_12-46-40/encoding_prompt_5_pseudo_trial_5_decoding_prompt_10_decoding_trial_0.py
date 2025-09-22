def decode_string():
    # Step 1: Receive input
    input_string = input().strip()  # Remove surrounding spaces from input

    # Step 2: Initialize variables
    index = 0
    output_string = ""

    # Step 3: Process the input string
    while index < len(input_string):
        if input_string[index] == '.':
            output_string += '0'  # Append '0' for a single dot
            index += 1  # Move to the next character
        elif index + 1 < len(input_string) and input_string[index + 1] == '.':
            output_string += '1'  # Append '1' for two dots
            index += 2  # Move past this pair of characters
        else:
            output_string += '2'  # Append '2' for any other character
            index += 2  # Move past this pair of characters (could be one or two)

    # Step 4: Output result
    print(output_string)

# You can call the function like this:
decode_string()
