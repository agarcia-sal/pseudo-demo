def convert_string_to_numeric(input_string):
    # Remove any leading or trailing whitespace
    input_string = input_string.strip()
    
    # Initialize an index variable to track our position in the input string
    current_index = 0
    # Initialize an empty string to hold the result
    result = ""
    
    # Loop until we have processed all characters in the input string
    while current_index < len(input_string):
        if input_string[current_index] == '.':
            # Append '0' if the current character is a '.'
            result += '0'
            # Move to the next character
            current_index += 1
        elif current_index + 1 < len(input_string) and input_string[current_index + 1] == '.':
            # Append '1' if the next character is also a '.'
            result += '1'
            # Skip the next character
            current_index += 2
        else:
            # For other characters, append '2'
            result += '2'
            # Move ahead by 2 characters
            current_index += 2
    
    # Output the final numeric string
    return result

# Function to handle input and output
def main():
    input_string = input()
    numeric_string = convert_string_to_numeric(input_string)
    print(numeric_string)

# Entry point of the program
if __name__ == "__main__":
    main()
