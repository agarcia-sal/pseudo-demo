# Start Main Program

# Step 1: Prompt the user for the first set of integers
first_set = input()
# Step 2: Prompt the user for the second set of integers
second_set = input()

# Step 3: Split Input Strings
first_list = first_set.split()  # Split the first set into a list of strings
second_list = second_set.split() # Split the second set into a list of strings

# Step 4: Initialize Difference Counter
difference_count = 0  # Variable to count the differences

# Step 5: Check Each Position for Differences
for index in range(3):  # Loop through the indices 0, 1, 2
    first_value = int(first_list[index])  # Convert string to integer from first list
    second_value = int(second_list[index])  # Convert string to integer from second list
    
    # If the values are different, increment the difference counter
    if first_value != second_value:
        difference_count += 1

# Step 6: Evaluate Number of Differences
if difference_count < 3:
    print("YES")  # Print YES if differences are less than 3
else:
    print("NO")   # Print NO otherwise
