# Starting point of the code
number_of_elements = int(input())  # Read the number of elements from input
is_active = [True] * number_of_elements  # Initialize a list with True values
index = 0  # Starting index
step = 1  # Initial step value

# Loop until step exceeds 500000
while step <= 500000:
    if is_active[index]:  # Check if the current index is active
        is_active[index] = False  # Mark the index as inactive
    step += 1  # Increment the step
    index = (index + step) % number_of_elements  # Calculate the new index

# Create a list of active elements still marked as True
active_elements = [elem for elem in is_active if elem]

# Check if there are any active elements remaining
if len(active_elements) == 0:
    print('YES')  # Print 'YES' if no elements are active
else:
    print('NO')  # Print 'NO' if there are active elements remaining
