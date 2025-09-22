# BEGIN PROGRAM

# Read input from standard input
a = input().strip()  # Read a line and remove whitespace from the beginning and end

# Replace occurrences of 'dot' with '.' and 'at' with '@'
a = a.replace('dot', '.').replace('at', '@')

# Check if the first character is a dot
if a.startswith('.'):
    a = 'dot' + a[1:]  # Concatenate 'dot' with the substring starting from index 1

# Initialize counter and list to store characters
co = 0  # Counter for '@' characters
c = []  # List to store characters
l = 0  # Length variable (not used in this implementation)

# Check if the first character is an at symbol
if a.startswith('@'):
    a = 'at' + a[1:]  # Concatenate 'at' with the substring starting from index 1

# Iterate over each character in a
for i in a:
    if i == '@':
        # Check if we have seen an '@' before
        if co > 0:
            c.append('at')  # Append 'at' to list c
            co = 1  # Set counter to 1
        else:
            c.append('@')  # Append '@' to list c
            co = 1  # Set counter to 1
    else:
        # Append the character to the list
        c.append(i)  # Append the current character

# Join list c into a single string
c = ''.join(c)  # Concatenate all elements in list c into a string

# Check if the last character is a dot
if c.endswith('.'):
    c = c[:-1] + 'dot'  # Concatenate 'dot' with the substring excluding the last character

# Output the final result
print(c)  # Print the final modified string

# END PROGRAM
