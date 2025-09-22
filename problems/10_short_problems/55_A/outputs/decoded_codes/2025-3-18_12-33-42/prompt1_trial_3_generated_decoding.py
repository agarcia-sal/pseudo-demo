# Step 1: Input size of the list
n = int(input())  # Read an integer value n

# Step 2: Initialize boolean list with all values set to True
b = [True] * n  # Create a boolean list b of length n initialized to True

# Step 3: Initialize counters
j = 0  # Track current index in b
i = 1  # Define the step size

# Step 4: Loop while i is less than or equal to 500,000
while i <= 500000:
    if b[j]:  # Check if the value at index j in b is True
        b[j] = False  # Mark the index as inactive by setting it to False
    i += 1  # Increment i by 1
    j = (j + i) % n  # Update j to be the new index, wrapping around if needed

# Step 5: Check results
x = [val for val in b if val]  # Create a list x of all True values from b

# Step 6: Output the result
if len(x) == 0:  # If there are no active indices
    print("YES")  # Output "YES"
else:
    print("NO")  # Otherwise output "NO"
