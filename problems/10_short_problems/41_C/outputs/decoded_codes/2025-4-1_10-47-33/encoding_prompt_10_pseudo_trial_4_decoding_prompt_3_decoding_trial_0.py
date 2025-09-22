def transform_input():
    # Read input from standard input
    a = input().strip()  # Remove any leading and trailing whitespace
    a = a.replace('dot', '.')  # Replace 'dot' with '.'
    a = a.replace('at', '@')    # Replace 'at' with '@'

    # Check if the first character is a dot
    if a.startswith('.'):
        a = 'dot' + a[1:]  # Replace the first character if it's a dot

    # Initialize counter and list to store characters
    co = 0  # Counter for occurrences of '@'
    c = []  # List to store characters
    l = 0   # Length of the string, not used in this implementation

    # Check if the first character is an at symbol
    if a.startswith('@'):
        a = 'at' + a[1:]  # Replace the first character if it's an '@'

    # Iterate over each character in a
    for i in a:
        if i == '@':
            # Check if we have seen an '@' before
            if co > 0:
                c.append('at')  # Append 'at' to list c
                co = 1
            else:
                c.append('@')  # Append '@' to list c
                co = 1
        else:
            c.append(i)  # Append the character to the list

    # Join list c into a single string
    result = ''.join(c)

    # Check if the last character is a dot
    if result.endswith('.'):
        result = result[:-1] + 'dot'  # Replace the last character if it's a dot

    # Output the final result
    print(result)

# Calling the function to execute the transformation
transform_input()
