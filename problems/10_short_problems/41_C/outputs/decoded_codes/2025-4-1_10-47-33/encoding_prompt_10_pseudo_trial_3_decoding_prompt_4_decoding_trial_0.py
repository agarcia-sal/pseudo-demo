def main():
    # Read input and remove leading/trailing whitespace
    a = input().strip()
    
    # Replace occurrences of 'dot' with '.' and 'at' with '@'
    a = a.replace('dot', '.').replace('at', '@')

    # If the first character is a dot, prepend 'dot'
    if a and a[0] == '.':
        a = 'dot' + a[1:]

    # Initialize a counter for '@' symbols and an empty list for characters
    co = 0
    chars = []

    # If the first character is an '@', prepend 'at'
    if a and a[0] == '@':
        a = 'at' + a[1:]

    # Iterate through each character in the input string
    for i in a:
        if i == '@':
            # Check if there is already an '@' in the list
            if co > 0:
                chars.append('at')
            else:
                chars.append('@')
            co += 1
        else:
            chars.append(i)
            co = 0  # Reset counter if we encounter a character other than '@'

    # Convert the list of characters back to a string
    c = ''.join(chars)

    # If the last character is a dot, replace it with 'dot'
    if c and c[-1] == '.':
        c = c[:-1] + 'dot'

    # Output the final result
    print(c)

# Call the main function to execute
main()
