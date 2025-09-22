# Function to process the input string
def process_input_string():
    # Read input and remove leading and trailing whitespace
    input_string = input().strip()
    
    # Replace 'dot' with '.' and 'at' with '@'
    input_string = input_string.replace('dot', '.')
    input_string = input_string.replace('at', '@')

    # Check if the first character is a dot
    if input_string.startswith('.'):
        input_string = 'dot' + input_string[1:]

    # Initialize counter and list to store characters
    counter = 0
    character_list = []
    
    # Check if the first character is an at symbol
    if input_string.startswith('@'):
        input_string = 'at' + input_string[1:]

    # Iterate over each character in the input string
    for character in input_string:
        if character == '@':
            # Check if we have seen an '@' before
            if counter > 0:
                character_list.append('at')
                counter = 1
            else:
                character_list.append('@')
                counter = 1
        else:
            # Append the character to the list
            character_list.append(character)
    
    # Join the list into a single string
    result_string = ''.join(character_list)

    # Check if the last character is a dot
    if result_string.endswith('.'):
        result_string = result_string[:-1] + 'dot'

    # Output the final result
    print(result_string)

# Call the function to execute the program
process_input_string()
