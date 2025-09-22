# Define a function to convert a string representation into a numeric string
def convert_string_to_numeric_string():
    # Read the input string and remove leading/trailing whitespace
    input_string = input().strip()
    
    # Initialize an index variable to iterate through the input string
    current_index = 0
    # Initialize an empty string to hold the resulting numeric string
    result = ""
    
    # Loop while the current index is less than the length of the input string
    while current_index < len(input_string):
        # Check if the current character is a dot
        if input_string[current_index] == '.':
            # Append '0' to result for a single dot
            result += '0'
            current_index += 1
        # Check if the next character is also a dot
        elif current_index + 1 < len(input_string) and input_string[current_index + 1] == '.':
            # Append '1' to result for two consecutive dots
            result += '1'
            current_index += 2
        else:
            # For other characters, append '2' to result
            result += '2'
            current_index += 2
            
    # Output the resulting numeric string
    print(result)

# You can call the function to test it
# convert_string_to_numeric_string()
