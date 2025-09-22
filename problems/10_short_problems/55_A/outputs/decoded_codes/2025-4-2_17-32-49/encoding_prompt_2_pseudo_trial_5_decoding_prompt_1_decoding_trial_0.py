# Step 1: Start (not explicitly represented in Python)

# Step 2: Input Requirement
totalElements = int(input())  # Read an integer value

# Step 3: Initialize
isActive = [True] * totalElements  # Create a list of size totalElements with all values set to True
index = 0  # Initialize index to 0
step = 1  # Initialize step to 1

# Step 4: Loop
while step <= 500000:  # Continue looping while step is less than or equal to 500,000
    if isActive[index]:  # Check if the current element is still True
        isActive[index] = False  # Mark it as inactive (set it to False)
    
    step += 1  # Increase the step variable by 1
    index = (index + step) % totalElements  # Update the index with the current step value and wrap around

# Step 5: Filter Active Elements
activeElements = [elem for elem in isActive if elem]  # Create a new list of active (True) elements

# Step 6: Output Requirement
if len(activeElements) == 0:  # Check if there are any active elements left
    print("YES")  # All elements have been marked inactive
else:
    print("NO")  # There are still active elements

# Step 7: End (not explicitly represented in Python)
