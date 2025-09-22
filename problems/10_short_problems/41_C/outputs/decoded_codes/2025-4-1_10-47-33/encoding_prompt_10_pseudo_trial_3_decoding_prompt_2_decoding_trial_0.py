# BEGIN Program

# Read input from standard input and remove leading/trailing whitespace
a = input().strip()

# Replace occurrences of 'dot' with '.' and 'at' with '@'
a = a.replace('dot', '.')
a = a.replace('at', '@')

# If the first character is a dot, prepend 'dot'
if a and a[0] == '.':
    a = 'dot' + a[1:]

# Initialize a counter for '@' symbols and list for characters
co = 0
c = []
l = 0

# If the first character is an '@', prepend 'at'
if a and a[0] == '@':
    a = 'at' + a[1:]

# Iterate through each character in a
for i in a:
    if i == '@':
        # Check if there is already an '@' in the list
        if co > 0:
            c.append('at')  # Add 'at' if '@' is already present
        else:
            c.append('@')   # Add '@' for the first occurrence
        co = 1  # Update the counter to indicate '@' is present
    else:
        c.append(i)  # Add the current character to the list

# Convert list c back to a string
c = ''.join(c)

# If the last character is a dot, replace it with 'dot'
if c and c[-1] == '.':
    c = c[:-1] + 'dot'  # Replacing the last dot with 'dot'

# Output the final result
print(c)

# END Program
