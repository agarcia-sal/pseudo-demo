# Begin Program

# Read input from standard input and remove leading/trailing whitespace
a = input().strip()

# Replace occurrences of 'dot' with '.' and 'at' with '@'
a = a.replace('dot', '.').replace('at', '@')

# If the first character is a dot, prepend 'dot'
if a.startswith('.'):
    a = 'dot' + a[1:]

# Initialize a counter for '@' symbols and list for characters
co = 0
c = []  # Create an empty list to hold the final characters

# If the first character is an '@', prepend 'at'
if a.startswith('@'):
    a = 'at' + a[1:]

# Iterate through each character in 'a'
for i in a:
    if i == '@':
        # Check if there is already an '@' in the list
        if co > 0:
            c.append('at')  # Add 'at' to the list if '@' already exists
        else:
            c.append('@')  # Add '@' to the list
        co = 1  # Set counter to indicate an '@' has been added
    else:
        c.append(i)  # Add the character to the list

# Convert list 'c' back to a string
c = ''.join(c)

# If the last character is a dot, replace it with 'dot'
if c.endswith('.'):
    c = c[:-1] + 'dot'  # Replace the last dot with 'dot'

# Output the final result
print(c)

# End Program
