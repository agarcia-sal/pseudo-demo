# Step 1: Input the size of the array
n = int(input())  # Taking input for the number of elements in the list

# Step 2: Initialize a list of Boolean values (all set to True)
b = [True] * n  # Create a list of size n filled with True values

# Step 3: Initialize variables for looping
j = 0  # Initialize j to 0
i = 1  # Initialize i to 1

# Step 4: Loop to process values while i is less than or equal to 500000
while i <= 500000:
    if b[j]:  # If the current position j in the list b is True
        b[j] = False  # Mark position j as False

    i += 1  # Increment i by 1
    j = (j + i) % n  # Update position j using modulo operation to wrap around

# Step 5: Create a new list x containing only True values from b
x = [a for a in b if a]  # List comprehension to filter True values

# Step 6: Check if the list x is empty and print the result
if len(x) == 0:  # If there are no True values left in b
    print("YES")  # Print "YES" indicating no True values remain
else:
    print("NO")  # Print "NO" indicating some True values are present
