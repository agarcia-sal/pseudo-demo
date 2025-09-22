def convert_input_to_binary_string():
    # Read input string from the user
    input_string = input()
    
    index = 0  # Initialize index to track position in the input string
    result_string = ""  # Initialize an empty string to hold the result
    
    # Iterate through the input string until the end
    while index < len(input_string):
        if input_string[index] == '.':
            # If current character is '.', append '0' to result
            result_string += '0'
            index += 1  # Move to the next character
        elif index + 1 < len(input_string) and input_string[index + 1] == '.':
            # If the next character is also '.', append '1' to result
            result_string += '1'
            index += 2  # Move past both characters
        else:
            # Otherwise, append '2' to result
            result_string += '2'
            index += 2  # Move past both characters
    
    # Output the result string
    print(result_string)

# Call the function to execute
convert_input_to_binary_string()
