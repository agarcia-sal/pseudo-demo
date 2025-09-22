def process_string():
    # Read input from standard input
    input_string = input()
    
    # Initialize index and output variable
    index = 0
    output = ""
    
    # Process the input string
    while index < len(input_string):
        if input_string[index] == '.':
            # Current character is '.', map it to '0'
            output += '0'
            index += 1
        elif index + 1 < len(input_string) and input_string[index + 1] == '.':
            # Next character is also '.', map the current to '1'
            output += '1'
            index += 2
        else:
            # Neither of the two characters is '.', map it to '2'
            output += '2'
            index += 2
    
    # Display the result
    print(output)

# Example test cases (these would run with actual use of the function)
# process_string()  # Input: "...a..b..." should yield: "001002"
