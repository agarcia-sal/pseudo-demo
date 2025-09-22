# This program compares two sets of three integers and checks how many are different.

# Step 1: Read the first set of integers from the user
first_set = input()  # Expected format: "1 2 3"

# Step 2: Read the second set of integers from the user
second_set = input()  # Expected format: "4 5 6"

# Step 3: Split the input strings into lists of integers
first_list = list(map(int, first_set.split()))  # Convert the first input to a list of integers
second_list = list(map(int, second_set.split()))  # Convert the second input to a list of integers

# Step 4: Initialize a counter for differences
difference_count = 0

# Step 5: Compare the corresponding integers from both lists
for index in range(3):  # Loop through the first three indices
    first_number = first_list[index]  # Get the first number from the first list
    second_number = second_list[index]  # Get the second number from the second list
    
    # Check if the numbers are different
    if first_number != second_number:
        difference_count += 1  # Increment the difference counter

# Step 6: Determine the output based on the number of differences
if difference_count < 3:
    print("YES")  # Print YES if fewer than three differences
else:
    print("NO")  # Print NO if three or more differences
