# BEGIN PROGRAM

# Read input from standard input
a = input().strip()  # Read a line from standard input and remove whitespace
a = a.replace('dot', '.')  # Replace all occurrences of 'dot' with '.'
a = a.replace('at', '@')  # Replace all occurrences of 'at' with '@'

# Check if the first character is a dot
if a.startswith('.'):
    a = 'dot' + a[1:]  # Concatenate 'dot' with the substring starting from index 1

# Initialize counter and list to store characters
co = 0  # Counter for '@'
c = []  # List to store characters
l = 0  # Length of the processed string

# Check if the first character is an at symbol
if a.startswith('@'):
    a = 'at' + a[1:]  # Concatenate 'at' with the substring starting from index 1

# Iterate over each character in a
for i in a:
    if i == '@':
        # Check if we have seen an '@' before
        if co > 0:
            c.append('at')  # Append 'at' to list c if '@' was seen before
        else:
            c.append('@')  # Append '@' to list c for the first occurrence
        co = 1  # Set co to indicate we have seen an '@'
    else:
        # Append the character to the list
        c.append(i)  # Append the current character to list c

# Join list c into a single string
c = ''.join(c)  # Concatenate all elements in list c

# Check if the last character is a dot
if c.endswith('.'):
    c = c[:-1] + 'dot'  # Replace the last character with 'dot'

# Output the final result
print(c)  # Print the final transformed string

# END PROGRAM
