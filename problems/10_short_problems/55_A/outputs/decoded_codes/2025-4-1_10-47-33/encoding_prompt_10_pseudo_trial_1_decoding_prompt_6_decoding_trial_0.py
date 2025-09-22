# Start Program

# Step 2: Input
n = int(input())  # Read an integer value from user input

# Step 3: Initialize Boolean Array
boolean_array = [True] * n  # Create a list of size n with all elements initialized to True

# Step 4: Initialize Counters
current_index = 0  # Represents the current index in the array
iteration_number = 1  # Represents the current iteration number

# Step 5: Loop Until Limit
while iteration_number <= 500000:
    # Check Boolean Condition
    if boolean_array[current_index]:  # Check if the current index in boolean_array is True
        boolean_array[current_index] = False  # Mark the current index as processed (set to False)
    
    iteration_number += 1  # Increment iteration_number by 1
    current_index = (current_index + iteration_number) % n  # Update current_index in a circular manner

# Step 6: Filter True Values
remaining_true_values = [value for value in boolean_array if value]  # Create a list of remaining True values

# Step 7: Output Result
if len(remaining_true_values) == 0:  # Check if there are no True values left
    print("YES")  # Output "YES" if the list is empty
else:
    print("NO")  # Output "NO" if there are remaining True values

# End Program
