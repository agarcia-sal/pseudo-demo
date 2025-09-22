# Step 1: Initialize Input
n = int(input())  # Read an integer representing the size of the list

# Step 2: Create a Boolean List
is_active = [True] * n  # Initialize a list of size n with all elements set to True

# Step 3: Set Up Variables
index = 0  # Initialize index to 0
counter = 1  # Initialize counter to 1

# Step 4: Iterate While Counter is Less Than or Equal To 500000
while counter <= 500000:
    if is_active[index]:  # If the current index is True
        is_active[index] = False  # Set it to False
    counter += 1  # Increment the counter
    index = (index + counter) % n  # Update index with wrap-around using modulo

# Step 5: Filter Active Elements
active_elements = [active for active in is_active if active]  # List of elements still True

# Step 6: Check Active Elements
if len(active_elements) == 0:  # If there are no active elements left
    print("YES")  # Output "YES"
else:
    print("NO")  # Otherwise output "NO"
