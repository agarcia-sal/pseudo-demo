# Step 1: Read Input
line = input()[:-1]  # omitting the last character

# Step 2: Determine Length
n = len(line)
rv = 0  # this will hold the result

# Step 3: Loop Through Lengths
for l in range(n):  # for each length l from 0 to n - 1
    for i in range(n):  # for each index i from 0 to n - 1
        # Check if the substring of length l starting from index i appears again:
        if line[i:i + l] in line[i + 1:]:  # check substring
            rv = l  # set rv to current length
            break  # exit the inner loop

# Step 4: Output Result
print(rv)
