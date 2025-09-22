# Start the Program

# Step 2: Receive Input
first_set = input()  # Prompt the user to enter the first set of three numbers
second_set = input()  # Prompt the user to enter the second set of three numbers

# Step 3: Split Input into Individual Numbers
first_list = first_set.split()  # Split first_set into a list
second_list = second_set.split()  # Split second_set into a list

# Step 4: Initialize a Counter for Differences
difference_count = 0  # Initialize difference counter

# Step 5: Compare Each Number in the Sets
for index in range(3):  # For each index from 0 to 2
    first_number = int(first_list[index])  # Convert first number to integer
    second_number = int(second_list[index])  # Convert second number to integer
    
    # If numbers are not equal, increment the difference counter
    if first_number != second_number:
        difference_count += 1

# Step 6: Determine the Result
if difference_count < 3:  # If fewer than 3 differences
    print("YES")  # Print "YES"
else:
    print("NO")  # Print "NO"

# Step 7: End the Program
