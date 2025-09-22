# Step 1: Receive an input value representing the number of elements
number_of_elements = int(input())

# Step 2: Create a list initialized to True
boolean_list = [True] * number_of_elements

# Step 3: Initialize variables
index = 0
step = 1

# Step 5: Process while step is less than or equal to 500,000
while step <= 500000:
    # Check if the current position in boolean_list is True
    if boolean_list[index]:
        # If it is True, set it to False
        boolean_list[index] = False
        
    # Increment step
    step += 1
    
    # Update index to wrap around using modulo
    index = (index + step) % number_of_elements

# Step 6: Collect all elements from boolean_list that are still True
true_elements = [value for value in boolean_list if value]

# Step 7: Check the length of true_elements
if len(true_elements) == 0:
    # Output "YES" if true_elements is empty
    print("YES")
else:
    # Output "NO" otherwise
    print("NO")
