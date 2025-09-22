# Step 1: Start by receiving input from the user
n = int(input())  # Read an integer from user, which determines the size of the list

# Step 2: Initialize a boolean list named statusList with n elements, all initialized to True
status_list = [True] * n

# Step 3: Initialize the variables
current_index = 0  # Current index to process in the list
increment = 1      # Increment value, starting from 1

# Step 4: Process the list
while increment <= 500000:  # Continue while the increment is less than or equal to 500,000
    if status_list[current_index]:  # Check if the current index in status_list is True
        status_list[current_index] = False  # Change that element to False
    
    increment += 1  # Increase increment by 1
    current_index = (current_index + increment) % n  # Update current_index with wrap around

# Step 5: Check remaining True values
remaining_true = [value for value in status_list if value]  # Create a new list of remaining True values

# Step 6: Generate output
if not remaining_true:  # If remaining_true is empty
    print("YES")
else:
    print("NO")  # Otherwise, print "NO"
