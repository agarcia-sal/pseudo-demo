def transform_input():
    # Read input from standard input and remove leading/trailing whitespace
    a = input().strip()

    # Replace occurrences of 'dot' with '.' and 'at' with '@'
    a = a.replace('dot', '.').replace('at', '@')

    # If the first character is a '.', prepend 'dot'
    if a.startswith('.'):
        a = 'dot' + a[1:]

    # Initialize a counter for '@' symbols and a list for characters
    co = 0  # Counter for the '@' symbols
    c = []  # List to hold the transformed characters

    # If the first character is an '@', prepend 'at'
    if a.startswith('@'):
        a = 'at' + a[1:]

    # Iterate through each character in the string
    for i in a:
        if i == '@':
            # Check if there is already an '@' in the list
            if co > 0:
                c.append('at')  # Append 'at' if another '@' is already present
                co = 1  # Reset counter
            else:
                c.append('@')  # Append single '@'
                co = 1  # Increment counter
        else:
            c.append(i)  # Add the character to the list

    # Convert list c back to a string
    result = ''.join(c)

    # If the last character is a '.', replace it with 'dot'
    if result.endswith('.'):
        result = result[:-1] + 'dot'  # Replace the last '.' with 'dot'

    # Output the final result
    print(result)

# Call the function to execute
transform_input()
