def convert_input_to_binary_string():
    # Read input from the standard input
    input_string = input()  # Input consisting of '.' characters
    index = 0  # Initialize an index to track the position in input_string
    result_string = ""  # Initialize an empty string to store the result

    # Loop until the index reaches the end of the input_string
    while index < len(input_string):
        # Check if the current character is '.'
        if input_string[index] == '.':
            result_string += '0'  # Append '0' for a single '.'
            index += 1  # Move to the next character
        # Check if the next character is also '.' for a '1' case
        elif index + 1 < len(input_string) and input_string[index + 1] == '.':
            result_string += '1'  # Append '1' for the pattern '..'
            index += 2  # Move past the next character as well
        else:
            result_string += '2'  # Append '2' for any unrecognized pattern
            index += 2  # Advance the index by 2

    # Print the resulting binary-like string
    print(result_string)

# Test the function with various input edge cases
if __name__ == "__main__":
    # Example tests
    # Input: "...."
    # Expected output: "000"
    convert_input_to_binary_string()  # Enter ".." for manual testing

    # Edge test cases
    # Input: "." -> Expected output: "0"
    # Input: ".." -> Expected output: "1"
    # Input: "....." -> Expected output: "100"
    # Input: "..." -> Expected output: "10"
    # Input: "..." -> Could test by running multiple times, or modify the input accordingly.
