# Step 1: Read input and initialize variables
line = input()
line = line[:-1]  # Remove the last character
n = len(line)
rv = 0  # This variable stores the result

# Step 2: Iterate through lengths l from 0 to n-1
for l in range(n):
    # Step 3: Check for substring presence
    for i in range(n):
        # Step 4: Check if the substring exists later in the string
        substring = line[i:i+l+1]  # Extract the substring
        if substring in line[i+1:]:  # Check if the substring exists later
            rv = l  # Update rv with the current length l
            break  # Exit the inner loop as the substring is found
    if rv == l:  # If we found a match break the outer loop as well
        break

# Step 5: Output the result
print(rv)  # Display the final value of rv
