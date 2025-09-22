# Start the Program

# Step 2: Receive Input
first_input = input()  # Get the first set of numbers from the user
second_input = input()  # Get the second set of numbers from the user

# Step 3: Split Input into Individual Numbers
first_set = first_input.split()  # Break the first set of numbers into a list
second_set = second_input.split()  # Break the second set of numbers into a list

# Step 4: Initialize a Difference Counter
difference_count = 0  # Set a variable to count differences

# Step 5: Compare Corresponding Numbers
for index in range(3):  # Loop through the indices 0 to 2
    first_number = int(first_set[index])  # Convert to integer
    second_number = int(second_set[index])  # Convert to integer
    if first_number != second_number:  # If they are different
        difference_count += 1  # Increment the difference counter

# Step 6: Check the Number of Differences
if difference_count < 3:  # If there are fewer than 3 differences
    print("YES")  # Output "YES"
else:  # Otherwise
    print("NO")  # Output "NO"

# End of Program
