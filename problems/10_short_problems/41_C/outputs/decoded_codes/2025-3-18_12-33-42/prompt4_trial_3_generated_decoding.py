def process_input():
    # Read input from the user
    a = input()

    # Replace occurrences of specific words with symbols
    a = a.replace('dot', '.').replace('at', '@')

    # If the string starts with a dot, change the first character
    if a.startswith('.'):
        a = 'dot' + a[1:]

    # Initialize variables for processing
    counter = 0
    characters = []
    
    # If the string starts with '@', change the first character
    if a.startswith('@'):
        a = 'at' + a[1:]

    # Iterate through each character in the string
    for i in a:
        if i == '@':
            if counter > 0:
                characters.append('at')
                counter = 1
            else:
                characters.append('@')
                counter = 1
        else:
            characters.append(i)

    # Join the characters list into a single string
    result = ''.join(characters)

    # If the result ends with a dot, replace it with 'dot'
    if result.endswith('.'):
        result = result[:-1] + 'dot'

    # Print the final output
    print(result)

# Call the function to execute the code
process_input()
