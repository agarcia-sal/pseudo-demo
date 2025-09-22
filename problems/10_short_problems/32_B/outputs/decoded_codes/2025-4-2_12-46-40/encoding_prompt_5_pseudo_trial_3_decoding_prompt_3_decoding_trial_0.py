def translate_dots_to_numbers():
    # Accept input from the user
    input_string = input().strip()  # Read and clean the input
    
    index = 0  # Initialize the index to track position in the input string
    result = ""  # Initialize an empty string to build the final output

    # Process the input until the end of the string
    while index < len(input_string):
        if input_string[index] == '.':  # If the current character is a dot
            result += '0'  # Append '0' to the result
            index += 1  # Move to the next position
        elif index + 1 < len(input_string) and input_string[index + 1] == '.': 
            # If the next character is also a dot
            result += '1'  # Append '1' to the result
            index += 2  # Move ahead by two positions
        else:  # If there is no dot or any other character
            result += '2'  # Append '2' to the result
            index += 2  # Move ahead by two positions

    # Output the final result
    print(result) 

# Call the function to run the program
translate_dots_to_numbers()
