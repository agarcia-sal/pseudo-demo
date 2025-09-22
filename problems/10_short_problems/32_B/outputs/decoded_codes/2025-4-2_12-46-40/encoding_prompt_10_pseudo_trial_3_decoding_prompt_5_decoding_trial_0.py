# Function to process the input string and generate the specified output
def process_input_string():
    # Step 1: Read input and initialize variables
    input_string = input().strip()  # Read input and remove trailing spaces
    index = 0  # Initialize the index for the while loop
    answer = ""  # Initialize the answer as an empty string

    # Step 2: Process each character in the input string
    while index < len(input_string):  # Loop until the end of the string
        if input_string[index] == '.':
            answer += '0'  # Append '0' if current character is '.'
            index += 1  # Increment index by 1
        elif index + 1 < len(input_string) and input_string[index + 1] == '.':
            answer += '1'  # Append '1' if next character is '.'
            index += 2  # Increment index by 2
        else:
            answer += '2'  # If no conditions are met, append '2'
            index += 2  # Increment index by 2

    # Step 3: Output the result
    print(answer)  # Print the generated answer

# Example usage
process_input_string()  # Call the function to execute
