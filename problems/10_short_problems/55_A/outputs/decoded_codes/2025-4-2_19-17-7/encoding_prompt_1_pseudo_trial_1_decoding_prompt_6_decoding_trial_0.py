# Step 1: Input the number of elements
number_of_elements = int(input())  # Read an integer value n from the user

# Step 2: Initialize a boolean list
is_prime = [True] * number_of_elements  # Create a list of size n, initialized to True

# Step 3: Initialize variables
step = 1  # Represents the current step in our iteration process
index = 0  # Tracks the current position in the is_prime list

# Step 4: Loop to iterate a maximum of 500,000 times
while step <= 500000:
    if is_prime[index]:  # Check if the current index in is_prime is True
        is_prime[index] = False  # Set the value at that position in is_prime to False
    
    step += 1  # Increment step by 1
    index = (index + step) % number_of_elements  # Update index using the formula

# Step 5: Collect remaining True values
remaining_true = [val for val in is_prime if val]  # Create a new list with all True values

# Step 6: Check the result
if not remaining_true:  # If remaining_true is empty
    print("YES")  # Output "YES"
else:
    print("NO")  # Otherwise, output "NO"
