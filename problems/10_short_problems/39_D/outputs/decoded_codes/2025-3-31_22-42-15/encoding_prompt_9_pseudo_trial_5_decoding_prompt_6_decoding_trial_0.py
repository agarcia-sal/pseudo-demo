# Start the main process.

# Step 2: Receive Input
first_set = input()  # Read the first line of input
second_set = input()  # Read the second line of input

# Step 3: Split Input into Lists
first_list = first_set.split()  # Split the first set into a list of strings
second_list = second_set.split()  # Split the second set into a list of strings

# Step 4: Initialize a Counter
difference_count = 0  # This will track the number of positions where the values differ

# Step 5: Compare Corresponding Values
for index in range(3):  # For each position from 0 to 2 (inclusive)
    value_from_first = int(first_list[index])  # Convert value from the first list to an integer
    value_from_second = int(second_list[index])  # Convert value from the second list to an integer
    
    if value_from_first != value_from_second:  # Check if they are not equal
        difference_count += 1  # Increment the difference counter

# Step 6: Evaluate the Result
if difference_count < 3:  # If the number of differences is less than 3
    print("YES")  # Output "YES"
else:
    print("NO")  # Otherwise, output "NO"

# End the main process.
