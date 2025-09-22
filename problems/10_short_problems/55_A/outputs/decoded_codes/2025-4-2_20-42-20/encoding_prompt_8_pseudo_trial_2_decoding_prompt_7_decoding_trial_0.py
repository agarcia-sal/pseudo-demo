# Step 1: Initialize Variables
n = int(input())  # Read an integer value n from input
b = [True] * n  # Create a list of size n filled with True values
j = 0  # Index tracking variable
i = 1  # Steps taken variable

# Step 2: Iterate to Mark Values
while i <= 500000:  # Limit the number of iterations to 500,000
    if b[j]:  # Check if the current index in list b is True
        b[j] = False  # Mark the value at index j as False
    
    i += 1  # Increment the step variable i
    j = (j + i) % n  # Update the index j, wrap around using modulo n

# Step 3: Check Remaining True Values
# Create a new list x that contains only the True values from list b
x = [value for value in b if value]

# Determine the result based on the length of x
if len(x) == 0:  # If no True values are left
    print("YES")  # Output "YES"
else:
    print("NO")  # Otherwise, output "NO"
