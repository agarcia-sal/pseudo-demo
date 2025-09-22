def convert_dots_to_digits():
    # Step 2: Read input and trim whitespace
    input_string = input().strip()
    
    # Step 3: Initialize variables
    index = 0
    result = ""
    
    # Step 4: Process the input string
    while index < len(input_string):
        if input_string[index] == '.':
            # Append '0' for single dot
            result += '0'
            index += 1
        elif index + 1 < len(input_string) and input_string[index + 1] == '.':
            # Append '1' for two consecutive dots
            result += '1'
            index += 2  # Skip the next character
        else:
            # Append '2' for other characters or single characters not followed by a dot
            result += '2'
            index += 2  # Skip the next character
    
    # Step 5: Output the result
    print(result)

# Function call to execute the conversion
convert_dots_to_digits()
