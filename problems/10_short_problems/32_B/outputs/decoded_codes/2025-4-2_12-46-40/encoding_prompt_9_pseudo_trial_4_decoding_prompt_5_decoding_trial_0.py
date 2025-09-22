# Function to convert a string of characters to a sequence of digits
def convert_string_to_digits():
    # Read input and trim whitespace
    input_string = input().strip()
    
    # Initialize variables
    index = 0
    result = ""
    
    # Process the input string
    while index < len(input_string):
        if input_string[index] == '.':
            result += '0'  # Append '0' for a single dot
            index += 1     # Move to the next character
        elif index + 1 < len(input_string) and input_string[index + 1] == '.':
            result += '1'  # Append '1' for two consecutive dots
            index += 2     # Skip the next character
        else:
            result += '2'  # Append '2' for other characters
            index += 2     # Skip the next character
    
    # Output the result
    print(result)

# Call the function to execute the conversion
convert_string_to_digits()
