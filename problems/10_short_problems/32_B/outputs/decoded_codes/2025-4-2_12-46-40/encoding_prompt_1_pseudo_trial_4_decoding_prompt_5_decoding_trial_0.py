def convert_string_to_numbers():
    # Read a line of input and remove any extra spaces from the beginning and end
    input_string = input().strip()
    
    # Initialize an index to traverse the string and a variable to store the result
    index = 0
    result = ''

    # Loop through the string until the end is reached
    while index < len(input_string):
        # Check if the current character is a period (.)
        if input_string[index] == '.':
            # If it's a period, append '0' to the result
            result += '0'
            # Move to the next character
            index += 1
        else:
            # Check if the next character is also a period (.)
            if index + 1 < len(input_string) and input_string[index + 1] == '.':
                # If the next character is a period, append '1' to the result
                result += '1'
                # Move the index forward by 2 characters
                index += 2
            else:
                # Append '2' to the result for any other character
                result += '2'
                # Move the index forward by 2 characters
                index += 2

    # Output the final result
    print(result)

# Example test cases (uncomment to test)
# Input: "...."
# Expected Output: "0000"

# Input: "....a.."
# Expected Output: "00012"

# Input: "a.b.c..d"
# Expected Output: "21212"
