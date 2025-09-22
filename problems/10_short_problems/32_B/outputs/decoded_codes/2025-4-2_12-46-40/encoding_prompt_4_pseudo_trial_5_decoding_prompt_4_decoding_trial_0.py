def process_string():
    # Read input from standard input
    s = input()

    # Initialize index and result variable
    index = 0
    output = ""

    # Process the input string
    while index < len(s):
        if s[index] == '.':
            # Current character is '.', map it to '0'
            output += '0'
            index += 1
        elif index + 1 < len(s) and s[index + 1] == '.':
            # Next character is also '.', map the current to '1'
            output += '1'
            index += 2
        else:
            # Neither of the two characters is '.', map it to '2'
            output += '2'
            index += 2

    # Display the result
    print(output)

# Call the function to execute the logic
process_string()
