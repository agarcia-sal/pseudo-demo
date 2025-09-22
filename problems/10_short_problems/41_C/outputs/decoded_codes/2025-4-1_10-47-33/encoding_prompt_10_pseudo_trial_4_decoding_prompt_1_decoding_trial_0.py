# BEGIN PROGRAM

# Read input from standard input
a = input()  # Read a line from standard input
a = a.strip()  # Remove whitespace from the beginning and end of a
a = a.replace('dot', '.')  # Replace all occurrences of 'dot' in a with '.'
a = a.replace('at', '@')  # Replace all occurrences of 'at' in a with '@'

# Check if the first character is a dot
if a.startswith('.'):
    a = 'dot' + a[1:]  # Set a to 'dot' concatenated with the substring of a starting from index 1

# Initialize counter and list to store characters
co = 0  # Counter
c = []  # Empty list c
l = 0  # Length (not used later)

# Check if the first character is an at symbol
if a.startswith('@'):
    a = 'at' + a[1:]  # Set a to 'at' concatenated with the substring of a starting from index 1

# Iterate over each character in a
for i in a:
    if i == '@':  # If the character is '@'
        if co > 0:  # Check if we have seen an '@' before
            c.append('at')  # Append 'at' to list c
            co = 1  # Set co to 1
        else:
            c.append('@')  # Append '@' to list c
            co = 1  # Set co to 1
    else:
        c.append(i)  # Append the character to the list

# Join list c into a single string
c = ''.join(c)  # Concatenate all elements in list c

# Check if the last character is a dot
if c.endswith('.'):
    c = c[:-1] + 'dot'  # Set c to substring of c excluding the last character, concatenated with 'dot'

# Output the final result
print(c)  # Print c

# END PROGRAM
