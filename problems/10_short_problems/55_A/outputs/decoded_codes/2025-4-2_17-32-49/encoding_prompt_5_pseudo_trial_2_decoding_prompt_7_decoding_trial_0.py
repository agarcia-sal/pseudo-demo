# Initialize Variables
n = int(input())  # Read an integer value for the size of the list
b = [True] * n  # Create a list of size n, initialized to True
j = 0  # Current position in the list
i = 1  # Iteration counter

# Process the List
while i <= 500000:
    # Check if the current position in list b is True
    if b[j]:
        b[j] = False  # Mark this position as visited
    i += 1  # Move to the next iteration
    j = (j + i) % n  # Update index j, wrapping around the list if necessary

# Determine Remaining Values
x = [value for value in b if value]  # Create a list of values that are still True

# Output the result based on the presence of True values
if len(x) == 0:
    print("YES")  # All positions were marked as visited
else:
    print("NO")  # Some positions remain unvisited
