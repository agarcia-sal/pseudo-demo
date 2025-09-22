# Function to process the input based on the provided requirements
def process_input():
    # Read input from standard input
    a = input().strip()  # Remove whitespace from edges

    # Replace 'dot' with '.' and 'at' with '@'
    a = a.replace('dot', '.').replace('at', '@')

    # Check if the first character is a dot
    if a.startswith('.'):
        a = 'dot' + a[1:]

    # Initialize counter and list to store characters
    co = 0
    c = []
    
    # Check if the first character is an at symbol
    if a.startswith('@'):
        a = 'at' + a[1:]

    # Iterate over each character in a
    for i in a:
        if i == '@':
            # Check if we have seen an '@' before
            if co > 0:
                c.append('at')
            else:
                c.append('@')
            co = 1  # Set counter to indicate we've encountered an '@'
        else:
            # Append the character to the list
            c.append(i)

    # Join list c into a single string
    c = ''.join(c)

    # Check if the last character is a dot
    if c.endswith('.'):
        c = c[:-1] + 'dot'

    # Output the final result
    print(c)

# Execute the function
process_input()
