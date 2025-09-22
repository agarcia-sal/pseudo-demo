def translate_dots_to_numbers():
    # Accept input from the user and clean it
    input_string = input().strip()
    
    # Initialize indices and result container
    index = 0
    result = ""

    # Process the input string
    while index < len(input_string):
        if input_string[index] == '.':
            result += "0"  # Encounter a dot
            index += 1  # Move to the next character
        elif index + 1 < len(input_string) and input_string[index + 1] == '.':
            result += "1"  # Encounter two dots in succession
            index += 2  # Skip the next dot
        else:
            result += "2"  # Encounter a non-dot character or the end
            index += 2  # Move ahead by two positions

    # Output the final result
    print(result)

# Call the function to execute the program
translate_dots_to_numbers()
