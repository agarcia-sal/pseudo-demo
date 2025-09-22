# BEGIN PROGRAM

# Read input from standard input
a = input().strip()  # Remove whitespace from the beginning and end of a
a = a.replace('dot', '.')  # Replace 'dot' with '.'
a = a.replace('at', '@')  # Replace 'at' with '@'

# Check if the first character is a dot
if a.startswith('.'):
    a = 'dot' + a[1:]  # Set a to 'dot' concatenated with the substring starting from index 1

# Initialize counter and list to store characters
co = 0
c = []  # Empty list to store characters

# Check if the first character is an at symbol
if a.startswith('@'):
    a = 'at' + a[1:]  # Set a to 'at' concatenated with the substring starting from index 1

# Iterate over each character in a
for i in a:
    if i == '@':
        # Check if we have seen an '@' before
        if co > 0:
            c.append('at')  # Append 'at' to the list
            co = 1
        else:
            c.append('@')  # Append '@' to the list
            co = 1
    else:
        c.append(i)  # Append the character to the list

# Join list c into a single string
c = ''.join(c)  # Combine all elements in list c into a string

# Check if the last character is a dot
if c.endswith('.'):
    c = c[:-1] + 'dot'  # Exclude the last character and concatenate with 'dot'

# Output the final result
print(c)

# END PROGRAM
