# Read input for the number of elements
number_of_elements = int(input())

# Initialize a boolean array to track the status of each position
boolean_array = [True] * number_of_elements

# Initialize variables for iteration
index = 0
step = 1

# Loop until the step exceeds 500,000
while step <= 500000:
    # If the current position is marked as True
    if boolean_array[index]:
        # Mark the current position as False
        boolean_array[index] = False
    
    # Move to the next step
    step += 1
    # Update the index by adding step and using modulo to keep it within bounds
    index = (index + step) % number_of_elements

# Create a list of all True values in the boolean array
true_values = [value for value in boolean_array if value]

# Check if there are no True values left
if len(true_values) == 0:
    print('YES')  # All positions were marked False
else:
    print('NO')   # There are still True positions left
