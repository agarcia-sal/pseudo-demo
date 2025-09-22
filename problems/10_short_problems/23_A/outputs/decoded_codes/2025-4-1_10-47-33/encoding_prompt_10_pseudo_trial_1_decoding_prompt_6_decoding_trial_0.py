# Step 1: Read input and initialize variables
line = input().strip()  # Read a line of input and remove any trailing newline
line = line[:-1]  # Remove the last character from line
n = len(line)  # Get the length of the line
result_value = 0  # This variable stores the result

# Step 2: Iterate through lengths l from 0 to n-1
for l in range(n):  # l will take values from 0 to n-1
    # Step 3: Check for substring presence
    for i in range(n):  # i will also take values from 0 to n-1
        # Step 4: Check if the substring exists later in the string
        substring = line[i:i+l]  # Extract the substring
        if substring and substring in line[i+1:]:  # Check for presence in the rest of the string
            result_value = l  # Update result_value with the current length l
            break  # Exit the inner loop as the substring is found

# Step 5: Output the result
print(result_value)  # Display the final value of result_value
