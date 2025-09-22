# Function to process the input string according to specified rules
def process_string():
    # Read input from standard input and strip whitespace
    input_string = input().strip()
    
    # Replace occurrences of specific words with symbols
    input_string = input_string.replace("dot", ".")
    input_string = input_string.replace("at", "@")

    # If the first character is '.', prepend 'dot'
    if input_string.startswith('.'):
        input_string = 'dot' + input_string[1:]

    # Initialize a counter and an empty list to hold characters
    counter = 0
    character_list = []

    # If the first character is '@', prepend 'at'
    if input_string.startswith('@'):
        input_string = 'at' + input_string[1:]

    # Process each character in input_string
    for character in input_string:
        if character == '@':
            if counter > 0:
                character_list.append('at')
                counter = 1
            else:
                character_list.append('@')
                counter = 1
        else:
            character_list.append(character)

    # Join the list of characters into a single string
    processed_string = ''.join(character_list)

    # If the last character is '.', replace it with 'dot'
    if processed_string.endswith('.'):
        processed_string = processed_string[:-1] + 'dot'

    # Output the final processed string
    print(processed_string)

# Optionally invoke the function if required in a script context
# process_string()  # Uncomment to run the function when script executes
