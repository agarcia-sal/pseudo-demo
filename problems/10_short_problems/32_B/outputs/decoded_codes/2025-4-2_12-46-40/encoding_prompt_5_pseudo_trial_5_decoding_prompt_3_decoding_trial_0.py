def decode_string():
    # Receive Input
    input_string = input().strip()  # Read a single line of input and remove surrounding spaces
    
    # Initialize Variables
    index = 0  # To track the current position in the input string
    output_string = ""  # To store the decoded result

    # Process Input String
    while index < len(input_string):
        if input_string[index] == '.':
            output_string += '0'  # Append '0' for a single dot
            index += 1  # Move to the next character
        elif index + 1 < len(input_string) and input_string[index + 1] == '.':
            output_string += '1'  # Append '1' for a pair of dots
            index += 2  # Move past this pair of characters
        else:
            output_string += '2'  # Append '2' for any other character
            index += 2  # Move past this pair of characters

    # Output Result
    print(output_string)

# To run the function:
decode_string()
