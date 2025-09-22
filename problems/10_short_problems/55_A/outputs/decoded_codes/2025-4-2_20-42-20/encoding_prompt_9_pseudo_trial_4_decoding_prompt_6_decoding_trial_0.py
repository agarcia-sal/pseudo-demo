# Step 1: Receive Input
n = int(input())  # Read an integer representing the size of the boolean list

# Step 2: Initialize Variables
boolean_list = [True] * n  # Create a list of size n with all elements set to True
index = 0  # This will track the current position in the list
counter = 1  # This will be used to determine how far to move in each iteration

# Step 3: Loop through a Range
while counter <= 500000:
    if boolean_list[index]:  # Check if the current element is True
        boolean_list[index] = False  # Mark it as processed by setting it to False
    counter += 1  # Increment counter by 1
    index = (index + counter) % n  # Update index with wrap around using modulo n

# Step 4: Check for Remaining True Values
remaining_true_values = [value for value in boolean_list if value]  # List of remaining True values

# Step 5: Determine Output
if len(remaining_true_values) == 0:  # Check if there are no remaining True values
    print("YES")  # All values have been processed
else:
    print("NO")  # Some values remain True
