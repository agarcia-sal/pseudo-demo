# Start Program

# Input:
n = int(input())

# Initialize Boolean Array:
b = [True] * n  # Create a list of size n with all values set to True

# Initialize Counters:
j = 0  # Current index in the array
i = 1  # Current iteration number

# Loop Until Limit:
while i <= 500000:
    # Check Boolean Condition:
    if b[j]:  # If the current index has not been marked
        b[j] = False  # Mark index j as processed
    i += 1  # Increment i by 1
    j = (j + i) % n  # Update j to the next index in a circular manner

# Filter True Values:
x = [value for value in b if value]  # Create a list of still True values from b

# Output Result:
if len(x) == 0:  # If no True values remain
    print("YES")
else:
    print("NO")

# End Program
