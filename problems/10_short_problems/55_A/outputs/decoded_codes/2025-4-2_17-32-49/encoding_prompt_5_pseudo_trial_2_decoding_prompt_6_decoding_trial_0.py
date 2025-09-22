# Initialize Variables
n = int(input())  # Read an integer value for size of the list
b = [True] * n   # Create a list of size n initialized with all values set to TRUE
j = 0             # Starting index
i = 1             # Iteration counter

# Process the List
while i <= 500000:  # Perform the operation for a fixed number of times
    if b[j]:      # Check if the value at index j is TRUE
        b[j] = False  # Mark this position as visited by setting it to FALSE
    i += 1          # Increment iteration counter
    j = (j + i) % n  # Update index j to the new position using modulo operation

# Determine Remaining Values
x = [value for value in b if value]  # Create a new list of all values that are still TRUE

# Output result based on the remaining TRUE values
if len(x) == 0:  # Check if there are no TRUE values left
    print("YES")  # Output YES if all positions were visited
else:
    print("NO")   # Output NO if some positions remain unvisited
