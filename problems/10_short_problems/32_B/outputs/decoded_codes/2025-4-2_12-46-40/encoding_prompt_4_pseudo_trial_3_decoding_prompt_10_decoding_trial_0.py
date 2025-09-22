def convert_dots_to_numbers():
    # Read a line of input and remove any whitespace
    input_string = input().strip()
    
    # Initialize index and result string
    index = 0
    result = ""

    # Loop until the end of the input string is reached
    while index < len(input_string):
        # Check if the current character is a single dot
        if input_string[index] == '.':
            result += '0'
            index += 1
        else:
            # Check the next character to determine the value to append
            if index + 1 < len(input_string) and input_string[index + 1] == '.':
                result += '1'
                index += 2
            else:
                result += '2'
                index += 2

    # Output the final result
    print(result)

# Optional: Add test cases to validate output
if __name__ == "__main__":
    # Example test runs
    # You can comment these out or replace with other test input
    print("Test 1 Input: '.. .. . ...'")
    # Expected Output: '012'
    convert_dots_to_numbers()

    print("Test 2 Input: '... . ..'")
    # Expected Output: '202'
    convert_dots_to_numbers()
