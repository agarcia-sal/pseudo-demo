# Define the main program logic
def process_string():
    # Read input string from standard input
    input_string = input()
    
    # Initialize index and result variables
    index = 0
    result = ''  # This will store the final output

    # Loop through each character of the string
    while index < len(input_string):
        # Check for a single dot
        if input_string[index] == '.':
            result += '0'  # Append '0' for a single dot
            index += 1  # Move to the next character
        else:
            # Check next character for a dot
            if index + 1 < len(input_string) and input_string[index + 1] == '.':
                result += '1'  # Append '1' for two consecutive dots
                index += 2  # Move past the two dots
            else:
                result += '2'  # Append '2' for other characters
                index += 2  # Move past the current character and its next one

    # Output the final result
    print(result)

# Call the function to execute the program
process_string()

# Test cases to consider:
# Input: "ab..c" => Output: "22"
# Input: ".abc" => Output: "02"
# Input: ".." => Output: "00"
# Input: "..." => Output: "00"
