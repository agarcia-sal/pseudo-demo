# This function converts a string of characters into a string of digits 
# based on specific conditions related to the presence of dots in the input string.

def convert_dots_to_digits():
    # Step 1: Read input and trim whitespace
    input_string = input().strip()
    
    # Step 2: Initialize index to track position and an empty result string
    index = 0
    result = ""

    # Step 3: Process the input string
    while index < len(input_string):
        # Check if the current character is a dot
        if input_string[index] == '.':
            # Append '0' for a dot and move to the next character
            result += '0'
            index += 1
        else:
            # Check the following character
            if index + 1 < len(input_string) and input_string[index + 1] == '.':
                # Append '1' for a dot followed character
                result += '1'
                index += 2  # Move two characters forward
            else:
                # Append '2' if the following character is not a dot
                result += '2'
                index += 2  # Move two characters forward

    # Step 4: Output the final result
    print(result)

# Call the function to execute
convert_dots_to_digits()
