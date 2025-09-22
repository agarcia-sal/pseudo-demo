def main():
    # Read input and remove leading/trailing spaces
    input_string = input().strip()
    
    # Initialize index and output string
    index = 0
    output_string = ""
    
    # Process input
    while index < len(input_string):
        current_char = input_string[index]
        
        # Check if the current character is a period
        if current_char == '.':
            output_string += '0'
            index += 1  # Move to the next character
        # Check if there is a next character and it is a period
        elif index + 1 < len(input_string) and input_string[index + 1] == '.':
            output_string += '1'
            index += 2  # Skip the current and the next character
        else:
            output_string += '2'
            index += 2  # Skip the current and the next character if no conditions met
    
    # Print the resulting output
    print(output_string)

# Call the main function to run the program
if __name__ == "__main__":
    main()
