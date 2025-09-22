# Begin the program
def process_input_string():
    # Step 1: Read input and initialize variables
    input_string = input().strip()  # Read the input and remove any trailing spaces
    index = 0  # Initialize the index for the loop
    answer = ""  # Initialize answer as an empty string

    # Step 2: Process each character in the input string
    while index < len(input_string):  # Continue until the end of the string
        # Check the character at the current index
        if input_string[index] == '.':
            answer += '0'  # Append '0' if current character is '.'
            index += 1  # Move to the next character
        # Check if there is a next character and it's a '.'
        elif index + 1 < len(input_string) and input_string[index + 1] == '.':
            answer += '1'  # Append '1' if the next character is '.'
            index += 2  # Skip both the current and next characters
        else:
            answer += '2'  # Append '2' for any other character
            index += 2  # Skip the current character and potentially the next one

    # Step 3: Output the result
    print(answer)  # Print the final answer string

# Call the function to execute the program
process_input_string()
