# Step 1: Initialize Input
n = int(input())  # Get an integer value n representing the number of boolean elements

# Step 2: Create Boolean List
booleanList = [True] * n  # Initialize a list of size n with all elements set to True

# Step 3: Set Initial Positions
currentIndex = 0  # Start at the first index of the boolean list
increment = 1  # Initial increment value to determine the position updates

# Step 4: Update Loop
limit = 500000  # Set a limit for the number of increments
while increment <= limit:
    if booleanList[currentIndex]:  # Check if the current index is True
        booleanList[currentIndex] = False  # Set the current index to False

    increment += 1  # Increase the increment for the next iteration
    # Update current index, ensuring it wraps around using modulo
    currentIndex = (currentIndex + increment) % n

# Step 5: Check Remaining True Values
remainingTrue = [value for value in booleanList if value]  # Create a list of remaining True values

# Step 6: Output Result
if len(remainingTrue) == 0:  # Check if there are any True values left
    print('YES')  # If none, output YES
else:
    print('NO')  # If there are still True values, output NO
