# Input the size of the list
n = int(input())

# Initialize the list status with all values set to True
status = [True] * n

# Set initial indices
current_index = 0
step = 1

# Loop until a limit is reached (step <= 500000)
while step <= 500000:
    if status[current_index]:  # Check if the current index is True
        status[current_index] = False  # Mark it as False
    step += 1  # Increment step
    current_index = (current_index + step) % n  # Update current index

# Create a list of remaining True values
remaining_true_values = [value for value in status if value]

# Determine and output the result
if len(remaining_true_values) == 0:
    print("YES")
else:
    print("NO")
