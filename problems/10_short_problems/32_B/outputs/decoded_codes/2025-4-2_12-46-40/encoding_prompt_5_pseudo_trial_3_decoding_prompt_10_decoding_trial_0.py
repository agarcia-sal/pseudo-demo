def translate_dots_to_numbers():
    # Step 1: Accept Input
    input_string = input().strip()  # Read input and remove any extra spaces or newlines
    
    # Step 2: Initialize Variables
    index = 0  # Track the current position
    result = ''  # Initialize an empty string for the final output

    # Step 3: Process Input
    while index < len(input_string):
        if input_string[index] == '.':  # If current character is a dot
            result += '0'  # Append '0' to the result
            index += 1  # Move to the next position
        elif index + 1 < len(input_string) and input_string[index + 1] == '.':  # Check for consecutive dots
            result += '1'  # Append '1' to the result
            index += 2  # Move ahead by two positions
        else:  # If neither condition matches
            result += '2'  # Append '2' to the result
            index += 2  # Move ahead by two positions

    # Step 4: Output the Result
    print(result)  # Display the final result string

# Example of running the function
translate_dots_to_numbers()
