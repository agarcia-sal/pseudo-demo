# Function to convert a string of '.' and '-' into a corresponding numerical string
def convert_characters_to_numbers():
    # Accept input string and clean it by removing surrounding spaces
    input_string = input().strip()
    
    # Initialize variables
    position = 0
    result = ""
    
    # Loop until we reach the end of the string
    while position < len(input_string):
        # Check if current character is a '.'
        if input_string[position] == '.':
            result += '0'  # Append '0' for a single dot
            position += 1   # Move to the next character
        # Check if the next character is a '.'
        elif position + 1 < len(input_string) and input_string[position + 1] == '.':
            result += '1'  # Append '1' for the sequence '.-'
            position += 2   # Skip two characters
        else:
            result += '2'  # Append '2' for the sequence '--'
            position += 2   # Skip two characters
  
    # Print the final result string
    print(result)

# Example of how to call the function
# convert_characters_to_numbers()  # Uncomment to test the function
