# Start Program

# Step 2: Receive Input
first_set = [int(x) for x in input().split()]  # Read first set of numbers and convert to integers
second_set = [int(x) for x in input().split()]  # Read second set of numbers and convert to integers

# Step 3: Initialize Difference Count
difference_count = 0  # This will keep track of how many numbers differ between the two sets

# Step 4: Loop through the Sets
for index in range(3):  # Loop over the three indices (0, 1, 2)
    if first_set[index] != second_set[index]:  # Check for differences
        difference_count += 1  # Increase count if numbers differ

# Step 5: Check the Number of Differences
if difference_count < 3:  # Check if less than three differences exist
    print("YES")  # Output "YES" if there are fewer than three differences
else:
    print("NO")  # Output "NO" if there are three or more differences

# End Program
