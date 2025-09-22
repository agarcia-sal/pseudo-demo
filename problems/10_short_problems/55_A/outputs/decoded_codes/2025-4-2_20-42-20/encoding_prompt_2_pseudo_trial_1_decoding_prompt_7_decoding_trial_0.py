# Start the program
# Step 2: Get the number of elements from the user
numberOfElements = int(input())

# Step 3: Create a list `isAvailable` initialized to True
isAvailable = [True] * numberOfElements

# Step 4: Initialize `index` and `increment`
index = 0
increment = 1

# Step 6: Loop while `increment` is less than or equal to 500000
while increment <= 500000:
    # Check if the current index is available
    if isAvailable[index]:
        isAvailable[index] = False  # Mark this index as unavailable
    
    # Step 8: Increase `increment` by 1
    increment += 1
    
    # Update index using modulo operation to wrap around
    index = (index + increment) % numberOfElements

# Step 7: Create a list `remainingTrue` that includes all True elements from `isAvailable`
remainingTrue = [value for value in isAvailable if value]

# Step 8: Check if there are any remaining True values
if len(remainingTrue) == 0:
    print('YES')  # Output 'YES' if no True values remain
else:
    print('NO')  # Output 'NO' if there are still True values
# End the program
