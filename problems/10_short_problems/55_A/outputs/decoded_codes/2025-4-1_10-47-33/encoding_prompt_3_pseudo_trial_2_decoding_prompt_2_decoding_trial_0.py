# Start of the program
numberOfElements = int(input())  # Step 1: Input for number of elements
isActive = [True] * numberOfElements  # Step 2: Create list of True values
index = 0  # Step 3: Initialize index
step = 1   # Initialize step

# Step 4: While loop to mark elements as inactive
while step <= 500000:
    if isActive[index]:  # Step 4a: Check if current index is active
        isActive[index] = False  # Step 4ai: Mark index as inactive
    step += 1  # Step 4b: Increment step
    index = (index + step) % numberOfElements  # Step 4c: Calculate new index

# Step 5: Create a list of active elements
activeElements = [elem for elem in isActive if elem]  # List comprehension to find remaining True values

# Step 6: Check the condition for active elements
if len(activeElements) == 0:  # Step 6a: No active elements remaining
    print('YES')  # Output if there are no active elements
else:  # Step 6b: Active elements still exist
    print('NO')  # Output if there are still active elements
