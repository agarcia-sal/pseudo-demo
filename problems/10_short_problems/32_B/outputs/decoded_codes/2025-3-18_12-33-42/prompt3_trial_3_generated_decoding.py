# Function to process the input string and generate the result string
def process_string():
    # Read a string 's' from standard input and trim whitespace
    s = input().strip()
    
    # Initialize the index and the result string
    index = 0
    result = ""

    # Loop until we reach the end of the input string
    while index < len(s):
        # Check if the current character is '.'
        if s[index] == '.':
            # Append '0' to the result
            result += '0'
            # Move to the next character
            index += 1
        else:
            # Check the next character
            if index + 1 < len(s) and s[index + 1] == '.':
                # Append '1' to the result
                result += '1'
                # Move forward by two characters
                index += 2
            else:
                # Append '2' to the result if the next character is not '.'
                result += '2'
                # Move forward by two characters
                index += 2

    # Output the result
    print(result)

# Call the function to execute the process
process_string()
