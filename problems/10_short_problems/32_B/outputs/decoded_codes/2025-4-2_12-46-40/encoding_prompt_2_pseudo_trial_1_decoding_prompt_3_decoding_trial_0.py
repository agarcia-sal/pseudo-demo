def generate_digits_from_dots():
    # Step 1: Read the input string and strip leading/trailing whitespace
    input_string = input().strip()
    
    # Step 2: Initialize index and result string
    index = 0
    result = ""
    
    # Step 4: Process each character in the input string
    while index < len(input_string):
        # Check if the current character is a dot
        if input_string[index] == '.':
            result += '0'
            index += 1  # Move to the next character
        else:
            # Check the next character, if it exists
            if index + 1 < len(input_string) and input_string[index + 1] == '.':
                result += '1'
                index += 2  # Move forward by two characters
            else:
                result += '2'
                index += 2  # Move forward by two characters

    # Step 5: Print the final result
    print(result)

# Testing the function
generate_digits_from_dots()
