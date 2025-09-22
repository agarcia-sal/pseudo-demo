# This function converts a specific string format into a numerical representation
def convert_string_to_numeric():
    # Receive input from the user
    input_string = input().strip()  # Read input and remove surrounding whitespace
    
    # Initialize variables
    index = 0  # To track the current position in the input string
    output_string = ""  # To store the resulting numeric representation
    
    # Process the input string
    while index < len(input_string):  # Loop until the end of the string
        if input_string[index] == '.':  # Check for a single dot
            output_string += '0'  # Append '0' for a single dot
            index += 1  # Move to the next character
        elif index + 1 < len(input_string) and input_string[index + 1] == '.':
            output_string += '1'  # Append '1' for a dot followed by another dot
            index += 2  # Skip to the character after the next
        else:
            output_string += '2'  # Append '2' for other characters
            index += 2  # Skip to the character after the next
    
    # Output the result
    print(output_string)  # Print the converted numeric representation

# Consider testing the function with different input scenarios:
# For example:  
# Input: "...". Expected Output: "000"
# Input: "..a.". Expected Output: "120"
# Edge case of input string being empty: Expected Output: ""
