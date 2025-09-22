# Initialize Variables
n = int(input())  # Read an integer value representing the size of the list
b = [True] * n    # Create a list of size n initialized with all values set to TRUE
j = 0             # Set index j to 0
i = 1             # Set index i to 1

# Process the List
while i <= 500000:
    if b[j]:  # Check if the value at index j in list b is TRUE
        b[j] = False  # Mark this position as visited
    i += 1   # Increment the value of i
    j = (j + i) % n  # Update index j to a new position using modulo n

# Determine Remaining Values
x = [value for value in b if value]  # Create a new list x that contains all TRUE values in b

# Output result based on the length of x
if len(x) == 0:
    print("YES")  # All positions were marked as visited
else:
    print("NO")   # Some positions remain unvisited
