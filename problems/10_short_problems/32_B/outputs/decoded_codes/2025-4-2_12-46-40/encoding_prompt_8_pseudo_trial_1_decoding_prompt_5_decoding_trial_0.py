# Function to translate a sequence of characters into a numeric string based on dot positions
def translate_dots_to_numbers():
    # Read input and remove extra spaces
    input_string = input().strip()
    
    # Initialize index and output string
    index = 0
    output_string = ""
    
    # Process input until the end of the string
    while index < len(input_string):
        # If the current character is a dot
        if input_string[index] == '.':
            output_string += '0'  # Append '0' to output
            index += 1  # Move to the next character
        # If the next character is also a dot
        elif index + 1 < len(input_string) and input_string[index + 1] == '.':
            output_string += '1'  # Append '1' to output
            index += 2  # Skip to the character after the next
        else:
            output_string += '2'  # Append '2' to output
            index += 2  # Skip to the character after the next

    # Output the final result
    print(output_string)

# Example test cases (uncomment to test)
# Input: "a..c"
# Output: "12"
# Input: ".b..d..f"
# Output: "010"
# Input: "xyz"
# Output: "2"
