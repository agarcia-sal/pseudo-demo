# Begin Program

# Read input from standard input
a = input().strip()  # Remove whitespace from the beginning and end
a = a.replace('dot', '.')  # Replace 'dot' with '.'
a = a.replace('at', '@')  # Replace 'at' with '@'

# Check if the first character is a dot
if a.startswith('.'):
    a = 'dot' + a[1:]  # Concatenate 'dot' with the rest of the string from index 1

# Initialize counter and list to store characters
co = 0  # Counter
c = []  # List to store characters

# Check if the first character is an at symbol
if a.startswith('@'):
    a = 'at' + a[1:]  # Concatenate 'at' with the rest of the string from index 1

# Iterate over each character in a
for i in a:
    if i == '@':
        # Check if we have seen an '@' before
        if co > 0:
            c.append('at')  # Append 'at' to list c
            co = 1  # Update counter
        else:
            c.append('@')  # Append '@' to list c
            co = 1  # Update counter
    else:
        # Append the character to the list
        c.append(i)

# Join list c into a single string
c = ''.join(c)  # Concatenate all elements in list c

# Check if the last character is a dot
if c.endswith('.'):
    c = c[:-1] + 'dot'  # Replace the last character with 'dot'

# Output the final result
print(c)

# End Program
