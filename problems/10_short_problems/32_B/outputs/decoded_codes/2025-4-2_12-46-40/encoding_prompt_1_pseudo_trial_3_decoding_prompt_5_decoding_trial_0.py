# Function to process the input string and generate the output based on specific rules
def process_string():
    # Read input string and remove leading/trailing whitespace
    input_string = input().strip()
    
    # Initialize index and output result
    index = 0
    result = ""
    
    # Loop through the string while the index is less than the length of the input string
    while index < len(input_string):
        # Check if the current character is a dot
        if input_string[index] == '.':
            # Append '0' to the result
            result += '0'
            # Move to the next character
            index += 1
        else:
            # Check if the next character is also a dot
            if index + 1 < len(input_string) and input_string[index + 1] == '.':
                # Append '1' to the result
                result += '1'
                # Move the index forward by two characters
                index += 2
            else:
                # Append '2' to the result as the next character is not a dot
                result += '2'
                # Move the index forward by two characters
                index += 2
    
    # Output the final result
    print(result)

# Example usage (this line would be removed in actual implementation)
# process_string()  # Uncomment this line to run the function
