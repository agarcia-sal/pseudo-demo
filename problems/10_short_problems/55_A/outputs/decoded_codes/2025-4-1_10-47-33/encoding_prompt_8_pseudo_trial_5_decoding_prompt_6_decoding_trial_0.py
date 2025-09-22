# Start the program
# Get user input
total_count = int(input())  # Read an integer named totalCount from the user.

# Initialize the list
is_marked = [True] * total_count  # Create a list called isMarked with totalCount entries, all set to True.

# Set counters
current_step = 1  # Set a counter named currentStep to 1.
index = 0  # Set a counter named index to 0.

# Processing loop
while current_step <= 500000:  # While currentStep is less than or equal to 500000
    if is_marked[index]:  # If isMarked at index is True
        is_marked[index] = False  # Mark this position as processed (set to False)
    
    current_step += 1  # Increment currentStep by 1
    index = (index + current_step) % total_count  # Update index with wrap-around using modulo

# Check results
remaining_true = [value for value in is_marked if value]  # Create a new list containing only True entries.

# Determine output
if len(remaining_true) == 0:  # If remainingTrue is empty (length is 0)
    print("YES")  # Output "YES"
else:
    print("NO")  # Otherwise, output "NO"
