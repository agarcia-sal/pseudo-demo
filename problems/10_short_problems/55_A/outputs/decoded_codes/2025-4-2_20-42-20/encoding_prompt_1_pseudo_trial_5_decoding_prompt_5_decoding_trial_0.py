# Start of the program

# Step 1: Read an integer number from user input
n = int(input())

# Step 2: Create a list called status with n elements, initialized to True
status = [True] * n

# Step 3: Initialize currentStep and index
current_step = 1
index = 0

# Step 4: Loop while currentStep is less than or equal to 500000
while current_step <= 500000:
    # Check the status of the current index
    if status[index]:
        # Set the current element to False if it's True
        status[index] = False
    
    # Increment currentStep by 1
    current_step += 1
    
    # Update the index for the next iteration
    index = (index + current_step) % n

# Step 5: Create a list of active elements (those that are still True)
active_elements = [element for element in status if element]

# Step 6: Check the result based on the number of active elements
if len(active_elements) == 0:
    print("YES")
else:
    print("NO")

# End of the program
