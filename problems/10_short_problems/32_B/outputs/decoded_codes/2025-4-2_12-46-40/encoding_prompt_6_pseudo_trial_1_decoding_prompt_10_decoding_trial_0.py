def convert_dot_notation_to_number():
    # Read input from the user
    input_string = input()
    
    # Initialize index and output variable
    index = 0
    output_string = ""

    # Loop through the entire input string
    while index < len(input_string):
        # Check if the current character is a single dot
        if input_string[index] == '.':
            # Append '0' to the output for a single dot
            output_string += '0'
            # Move to the next character
            index += 1
            
        else:
            # Check the next character
            if index + 1 < len(input_string) and input_string[index + 1] == '.':
                # Append '1' to the output for a pair of dots
                output_string += '1'
                # Move the index forward by 2 characters
                index += 2
                
            else:
                # Append '2' for a pair where the first is dot and the second is not
                output_string += '2'
                # Move the index forward by 2 characters
                index += 2

    # Output the final result
    print(output_string)

# Test the function with various test cases
if __name__ == "__main__":
    print("Test Case 1:")
    convert_dot_notation_to_number()  # Example: "...." should output 0000
    print("Test Case 2:")
    convert_dot_notation_to_number()  # Example: "..a" should output 21
    print("Test Case 3:")
    convert_dot_notation_to_number()  # Example: ".aa.." should output 202
    print("Test Case 4:")
    convert_dot_notation_to_number()  # Example: "a.a.a" should output 202
    print("Test Case 5:")
    convert_dot_notation_to_number()  # Example: "..." should output 000
