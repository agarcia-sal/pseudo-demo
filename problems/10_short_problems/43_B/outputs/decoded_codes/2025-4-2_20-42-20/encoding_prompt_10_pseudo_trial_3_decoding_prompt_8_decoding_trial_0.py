# Begin Program

# Initialize a list s1
s1 = []
# Initialize a list s2
s2 = []

# Read first input and store it in variable 'first_input'
first_input = input()
# Read second input and store it in variable 'second_input'
second_input = input()

# For each character in 'first_input':
for char in first_input:
    # If the character is not a space:
    if char != ' ':
        # Add the character to list s1
        s1.append(char)

# For each character in 'second_input':
for char in second_input:
    # If the character is not a space:
    if char != ' ':
        # Add the character to list s2
        s2.append(char)

# Initialize a list freqs to store frequency differences
freqs = []

# For each integer x from the ASCII value of 'A' to the ASCII value of 'z':
for x in range(ord('A'), ord('z') + 1):
    # Count the occurrences of the character corresponding to x in s1
    count_s1 = s1.count(chr(x))
    # Count the occurrences of the character corresponding to x in s2
    count_s2 = s2.count(chr(x))
    # Subtract the count from s2 from the count from s1
    freqs.append(count_s1 - count_s2)

# Count the number of elements in freqs that are less than 0
count_negative = sum(1 for freq in freqs if freq < 0)

# If the count is equal to 0:
if count_negative == 0:
    # Output "YES"
    print("YES")
# Else:
else:
    # Output "NO"
    print("NO")

# End Program
