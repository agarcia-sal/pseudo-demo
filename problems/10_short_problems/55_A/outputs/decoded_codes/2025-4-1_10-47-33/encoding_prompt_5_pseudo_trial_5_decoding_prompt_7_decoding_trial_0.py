# Start of the program

# Step 1: Accept the size of the boolean list from user input
n = int(input())  # Read the size of the boolean list

# Step 2: Create a boolean list of size n with all values initially set to True
booleanList = [True] * n  # Initialize all values to True

# Step 3: Initialize index variables
currentIndex = 0  # Starting index
increment = 1     # Increment value

# Step 4: Loop to update the boolean list
while increment <= 500000:  # Continue for a maximum of 500000 increments
    # Step 4a: If the value at the current index is True
    if booleanList[currentIndex]:  # Check if the current value is True
        # Step 4b: Set the value at the current index to False
        booleanList[currentIndex] = False  # Toggle the value to False
        
    # Step 4c: Update the increment and move to the next index
    increment += 1  # Increase the increment by 1
    currentIndex = (currentIndex + increment) % n  # Update index with wrap-around
              
# Step 5: Check for any True values left in the boolean list
remainingTrueValues = [value for value in booleanList if value]  # Filter to find any True values

# Step 6: Determine the result based on the presence of True values
if len(remainingTrueValues) == 0:  # If there are no True values left
    print("YES")  # Output "YES" if all are False
else:
    print("NO")   # Output "NO" if there are still True values present

# End of the program
