def process_input():
    # Step 2: Read Input and trim leading/trailing spaces
    input_string = input().strip()
    
    # Step 3: Initialize Variables
    index = 0
    output_string = ""

    # Step 4: Process Input
    while index < len(input_string):
        if input_string[index] == '.':
            # If the current character is a period
            output_string += '0'
            index += 1  # Move to the next character
        elif index + 1 < len(input_string) and input_string[index + 1] == '.':
            # If the next character is a period
            output_string += '1'
            index += 2  # Skip both characters
        else:
            # If neither is a period
            output_string += '2'
            index += 2  # Skip both characters

    # Step 5: Output Result
    print(output_string)

# Call the function to execute the code
process_input()
