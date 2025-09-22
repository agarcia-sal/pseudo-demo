def convert_encoded_string_to_decimal(s):
    # Read input string and remove any extra whitespace
    stripped_input_string = s.strip()  # Trim whitespace

    # Initialize index and output result variable
    index = 0
    result_string = ''

    # Loop through the input string while there are remaining characters
    while index < len(stripped_input_string):  # Iterate until we've processed the string
        # Check for the encoding pattern represented by a single dot
        if stripped_input_string[index] == '.':
            # Append '0' for a single dot
            result_string += '0'
            # Move to the next character
            index += 1

        # Check for the encoding pattern represented by two dots
        elif index + 1 < len(stripped_input_string) and stripped_input_string[index + 1] == '.':
            # Append '1' for two dots
            result_string += '1'
            # Skip the next character as it's part of the encoding
            index += 2

        # If neither pattern matches, it represents two dots and a dash
        else:
            # Append '2' for two dots and a dash
            result_string += '2'
            # Skip the next character as it's part of the encoding
            index += 2

    # Output the final converted result
    print(result_string)  # Display the output

# Example test cases to validate the function
if __name__ == '__main__':
    # Test cases for various encoded strings
    test_cases = [
        " . .. .... ",  # Should print "012"
        "......",       # Should print "111"
        "....-..",      # Should print "222"
        ". .. . . .",    # Should print "01010"
        ".....",        # Should print "111"
        ". .. .. -",    # Should print "0102"
        ""              # Should print ""
    ]

    for test in test_cases:
        print(f"Input: '{test}' -> Output: ", end="")
        convert_encoded_string_to_decimal(test)
