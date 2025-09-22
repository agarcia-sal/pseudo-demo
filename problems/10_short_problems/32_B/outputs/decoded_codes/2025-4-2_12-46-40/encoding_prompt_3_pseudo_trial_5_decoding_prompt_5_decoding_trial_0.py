# This program processes a given string based on specific character patterns and generates a result string.

def process_string():
    # Read input from standard input and trim whitespace
    string_representation = input().strip()
    
    # Initialize variables
    index = 0
    result_string = ""

    # Continue processing until the end of the string is reached
    while index < len(string_representation):
        # Check the current character at the index
        if string_representation[index] == '.':
            # If current character is '.', append '0' to the result
            result_string += '0'
            index += 1
        elif index + 1 < len(string_representation) and string_representation[index + 1] == '.':
            # If the next character is also '.', append '1' to the result
            result_string += '1'
            index += 2
        else:
            # If neither condition is satisfied, append '2' to the result
            result_string += '2'
            index += 2

    # Output the final result string
    print(result_string)

# Example test cases (uncomment to run)
# process_string()  # Input: "..a..b..." should output "01"

