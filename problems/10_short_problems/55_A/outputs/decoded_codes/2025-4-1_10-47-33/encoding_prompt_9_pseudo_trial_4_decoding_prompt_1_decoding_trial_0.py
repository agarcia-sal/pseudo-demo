# Read Input
n = int(input())  # Read an integer value representing the number of elements.

# Initialize List
marked = [True] * n  # Create a list with n elements, initialized to True.

# Initialize Counters
current_index = 0  # Position currently being processed.
step_size = 1      # Increment for marking process.

# Iterative Marking
while step_size <= 500000:
    if marked[current_index]:  # Check if the current position is still marked as True.
        marked[current_index] = False  # Mark it as False.
    step_size += 1  # Increment the step size.
    current_index = (current_index + step_size) % n  # Calculate the next position to check.

# Check Marks
remaining_true = [x for x in marked if x]  # Create a list of elements still marked as True.

# Output Result
if len(remaining_true) == 0:  # If no elements remain true
    print("YES")  # Output "YES"
else:
    print("NO")  # Output "NO"
