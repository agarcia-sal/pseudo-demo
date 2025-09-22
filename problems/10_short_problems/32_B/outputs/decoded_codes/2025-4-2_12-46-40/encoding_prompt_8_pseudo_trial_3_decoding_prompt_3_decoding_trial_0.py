# Function to convert the input string into a numerical representation
def translate_string_to_numbers():
    # Step 1: Read and process the input
    input_string = input().strip()  # Read input and remove extra spaces

    # Step 2: Initialize variables
    current_position = 0  # Start at the beginning of the string
    result = ""  # This will hold the final output

    # Step 3: Process the input string
    while current_position < len(input_string):
        # Check if the current character is a dot
        if input_string[current_position] == '.':
            result += '0'  # Single dot corresponds to '0'
            current_position += 1  # Move to the next character

        # Check if there's a next character and if it's also a dot
        elif (current_position + 1 < len(input_string) and 
              input_string[current_position + 1] == '.'):
            result += '1'  # Pair of dots corresponds to '1'
            current_position += 2  # Move past both dots

        else:
            result += '2'  # Any other character configuration corresponds to '2'
            current_position += 2  # Move past the two characters

    # Step 4: Print the final result
    print(result)  # Output the numerical representation

# Invoke the function to test its functionality
translate_string_to_numbers()
