# Step 1: Initialize Variables
n = int(input())  # Read an integer value from user input
b = [True] * n  # Create a list filled with 'True' values of size 'n'
j = 0  # Initialize the index tracker
i = 1  # Initialize the step counter

# Step 2: Iterate to Mark Values
while i <= 500000:  # Continue until i exceeds 500,000
    if b[j]:  # Check if the current index in list b is 'True'
        b[j] = False  # Mark the current index as 'False'
    i += 1  # Increment i by 1
    j = (j + i) % n  # Update index j and wrap around if necessary

# Step 3: Check Remaining True Values
x = [value for value in b if value]  # Create a list of remaining 'True' values

# Step 4: Output the result
if len(x) == 0:  # If no 'True' values remain
    print("YES")  # Output "YES"
else:
    print("NO")  # Otherwise, output "NO"
