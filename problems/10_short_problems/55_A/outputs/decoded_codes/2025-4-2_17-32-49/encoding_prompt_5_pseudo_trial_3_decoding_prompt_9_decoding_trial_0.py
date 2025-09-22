# Step 1: Start Program

# Step 2: Receive Input
n = int(input())  # Read a number n representing the size of the list

# Step 3: Initialize Boolean List
booleanList = [True] * n  # Create a boolean list of size n with initial values True

# Step 4: Set Up Iteration Variables
currentIndex = 0  # This will track the position in booleanList
step = 1  # This will dictate the increment step

# Step 5: Mark Elements Process
while step <= 500000:  # Work through steps until 500000
    # Step 5.1: Check Current Position
    if booleanList[currentIndex]:  # If the position is still True (unmarked)
        booleanList[currentIndex] = False  # Mark this position as False (marked)
    
    # Step 5.2: Increment Step Value
    step += 1  # Increase step for next iteration
    
    # Step 5.3: Calculate Next Position
    currentIndex = (currentIndex + step) % n  # Update index, wrapping with modulo n

# Step 6: Extract Remaining Unmarked Elements
remainingTrue = [value for value in booleanList if value]  # List of still true (unmarked) values

# Step 7: Check Results
if len(remainingTrue) == 0:  # If there are no unmarked positions
    print("YES")  # All positions were marked
else:
    print("NO")  # At least one position remained unmarked

# Step 8: End Program
