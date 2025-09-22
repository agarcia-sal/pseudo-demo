# Initialize Variables

# Read size of the list from user input
n = int(input())

# Create a list initialized with all values set to True
b = [True] * n

# Initialize index variables
j = 0  # Current position in the list
i = 1  # Iteration count

# Process the List
while i <= 500000:
    if b[j]:  # Check if the current position is still True
        b[j] = False  # Mark this position as visited
    i += 1  # Increment the iteration count
    j = (j + i) % n  # Update index j with wrap-around

# Determine Remaining Values
x = [value for value in b if value]  # Filter the list to get remaining True values

# Output result based on remaining values
if len(x) == 0:
    print("YES")  # All positions were marked as visited
else:
    print("NO")   # Some positions remain unvisited
