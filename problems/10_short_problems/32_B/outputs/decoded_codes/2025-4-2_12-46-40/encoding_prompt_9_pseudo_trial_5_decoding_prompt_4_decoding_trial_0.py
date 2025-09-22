# Function to convert a specific string format into a numerical representation
def convert_string_to_numbers():
    # Step 1: Receive Input
    input_string = input().strip()  # Read input and remove surrounding whitespace

    # Step 2: Initialize Variables
    index = 0  # To track the current position in the input string
    output_string = ""  # To store the resulting numeric representation

    # Step 3: Process the Input String
    while index < len(input_string):
        # Check if the current character is a dot
        if input_string[index] == '.':
            output_string += '0'  # Append '0' for single dot
            index += 1  # Move to the next character
        # Check if the next character is a dot
        elif index + 1 < len(input_string) and input_string[index + 1] == '.':
            output_string += '1'  # Append '1' for a dot pair
            index += 2  # Skip to the character after the next
        else:
            output_string += '2'  # Append '2' for other cases
            index += 2  # Skip to the character after the next

    # Step 4: Output the Result
    print(output_string)  # Print the converted numeric representation

# Call the function to execute the conversion
convert_string_to_numbers()
