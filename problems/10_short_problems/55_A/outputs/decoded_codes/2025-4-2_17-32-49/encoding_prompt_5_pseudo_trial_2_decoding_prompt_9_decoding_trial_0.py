# Initialize Variables
n = int(input())  # Read an integer value for the size of the list
b = [True] * n  # Create a list of size n initialized to TRUE
j = 0  # Initialize the index j
i = 1  # Initialize the iteration counter i

# Process the List
while i <= 500000:
    if b[j]:  # Check if the current position is TRUE
        b[j] = False  # Mark this position as visited by setting it to FALSE
    i += 1  # Increment the iteration counter
    j = (j + i) % n  # Update index j with wrapping

# Determine Remaining Values
x = [value for value in b if value]  # Create a new list of remaining TRUE values

# Output result based on the length of x
if len(x) == 0:
    print("YES")  # All positions were visited
else:
    print("NO")  # Some positions remain unvisited
