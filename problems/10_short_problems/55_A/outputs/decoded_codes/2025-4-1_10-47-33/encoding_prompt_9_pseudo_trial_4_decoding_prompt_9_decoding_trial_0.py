# Read input for the number of elements
n = int(input())

# Initialize the marked list with True values
marked = [True] * n

# Initialize index and step size
current_index = 0
step_size = 1

# Iterative marking process
while step_size <= 500000:
    if marked[current_index]:  # Check if current position is marked true
        marked[current_index] = False  # Mark it as false
    step_size += 1  # Increment the step size
    current_index = (current_index + step_size) % n  # Calculate next position

# Create a list of remaining true values
remaining_true = [x for x in marked if x]

# Output the result
if len(remaining_true) == 0:  # If no remaining true values
    print("YES")
else:
    print("NO")
