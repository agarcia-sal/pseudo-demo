# Begin the program

# Read input from standard input and remove leading/trailing whitespace
a = input().strip()

# Replace occurrences of 'dot' with '.' and 'at' with '@'
a = a.replace('dot', '.')
a = a.replace('at', '@')

# If the first character is a dot, prepend 'dot'
if a.startswith('.'):
    a = 'dot' + a[1:]

# Initialize a counter for '@' symbols and an empty list for characters
co = 0
c = []
l = 0

# If the first character is an '@', prepend 'at'
if a.startswith('@'):
    a = 'at' + a[1:]

# Iterate through each character in a
for i in a:
    if i == '@':
        # Check if there is already an '@' in the list
        if co > 0:
            c.append('at')
            co = 1  # Ensures only one '@' can occur
        else:
            c.append('@')
            co = 1  # Set to indicate '@' has been added
    else:
        c.append(i)  # Add other characters directly to the list

# Convert the list c back to a string
c = ''.join(c)

# If the last character is a dot, replace it with 'dot'
if c.endswith('.'):
    c = c[:-1] + 'dot'

# Output the final result
print(c)

# End of program
