# Step 1: Read input and initialize variables
line = input()  # Read a line of input
line = line[:-1]  # Remove the last character from line
n = len(line)  # Set n to the length of line
rv = 0  # This variable stores the result

# Step 2: Iterate through lengths l from 0 to n-1
for l in range(n):  # l takes values from 0 to n-1
    # Step 3: Check for substring presence
    for i in range(n):  # i takes values from 0 to n-1
        # Step 4: Check if the substring exists later in the string
        if line[i:i+l] in line[i+1:]:  # Check if the substring exists later in the string
            rv = l  # Update rv with the current length l
            break  # Exit the inner loop as the substring is found

# Step 5: Output the result
print(rv)  # Display the final value of rv
