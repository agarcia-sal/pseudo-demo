# Function to encode the input string into a result based on specific rules
def encode_string():
    # Read input string from standard input
    input_string = input()
    
    # Initialize index and result string
    index = 0
    result = ''
    
    # Loop until all characters in the string have been processed
    while index < len(input_string):
        # Check the current character
        if input_string[index] == '.':
            # Append '0' to the result for a single dot
            result += '0'
            index += 1
        elif index + 1 < len(input_string) and input_string[index + 1] == '.':
            # Append '1' to the result for a dot followed by another dot
            result += '1'
            index += 2
        else:
            # Append '2' for any other scenario
            result += '2'
            index += 2
    
    # Output the result string
    print(result)

# Example test case comments:
# Input: ".." should output "1"
# Input: "..." should output "0"
# Input: "....x" should output "20"
