# Start the main process

# Step 2: Receive Input
first_set = input()    # Read the first line of input
second_set = input()   # Read the second line of input

# Step 3: Split Input into Lists
first_list = first_set.split()   # Split the first set into a list of strings
second_list = second_set.split()  # Split the second set into a list of strings

# Step 4: Initialize a Counter
difference_count = 0  # This will track the number of differing positions

# Step 5: Compare Corresponding Values
for index in range(3):  # Loop over the indices 0 to 2
    # Convert each value to an integer for comparison
    value_from_first = int(first_list[index])
    value_from_second = int(second_list[index])
    
    # If the values differ, increment the counter
    if value_from_first != value_from_second:
        difference_count += 1

# Step 6: Evaluate the Result
if difference_count < 3:
    print("YES")  # Print YES if the difference count is less than 3
else:
    print("NO")   # Print NO otherwise

# End the main process
