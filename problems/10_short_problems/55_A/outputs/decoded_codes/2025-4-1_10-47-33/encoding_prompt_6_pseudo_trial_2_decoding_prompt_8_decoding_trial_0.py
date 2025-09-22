# Step 1: Receive input value for n
numberOfElements = int(input())

# Step 2: Initialize a boolean list to track elements
isActive = [True] * numberOfElements

# Step 3: Initialize index variables for the loop
index = 0
increment = 1

# Step 4: Loop through numbers while the increment value is less than or equal to 500,000
while increment <= 500000:
    # Step 5: Check if the current index in the boolean list is active
    if isActive[index]:
        # Step 6: Mark the current index as inactive
        isActive[index] = False
    
    # Step 7: Move to the next increment
    increment += 1
    
    # Step 8: Update the index based on the current increment while ensuring it wraps around
    index = (index + increment) % numberOfElements

# Step 9: Create a list of active elements from the boolean list
activeElements = [i for i in range(numberOfElements) if isActive[i]]

# Step 10: Check if there are active elements left
if len(activeElements) == 0:
    # Step 11: If no active elements, output 'YES'
    print('YES')
else:
    # Step 12: Otherwise, output 'NO'
    print('NO')
