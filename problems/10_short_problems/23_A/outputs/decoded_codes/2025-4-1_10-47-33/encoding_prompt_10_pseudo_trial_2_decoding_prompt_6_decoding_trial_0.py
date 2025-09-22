# Step 1: Read Input
line = input()[:-1]  # Read input string and omit the last character

# Step 2: Determine Length
n = len(line)  # Length of the string
result_value = 0  # This will hold the result

# Step 3: Loop Through Lengths
for length in range(n):  # Loop from 0 to n-1
    for index in range(n):  # Loop from 0 to n-1
        # Check if the substring of length 'length' starting at 'index' appears again in 'line'
        if line[index:index + length] in line[index + 1:]:
            result_value = length  # Set result_value to 'length'
            break  # Exit the inner loop as no further checks are needed for this length

# Step 4: Output Result
print(result_value)  # Print the final result
