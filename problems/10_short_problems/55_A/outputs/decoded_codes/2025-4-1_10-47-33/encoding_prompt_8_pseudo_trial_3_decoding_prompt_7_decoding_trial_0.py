# Begin Program

# Step 1: Get Input
n = int(input())  # Read a number n which represents the number of positions in a list.

# Step 2: Initialize List
marked = [True] * n  # Create a list 'marked' of size n filled with True.

# Step 3: Set Initial Variables
currentIndex = 0  # This will track the current position.
step = 1  # This will determine the step size for marking.

# Step 4: Mark Unmarked Positions
while step <= 500000:  # Continue marking while step is less than or equal to 500000.
    if marked[currentIndex]:  # Check if the position at currentIndex is True (unmarked).
        marked[currentIndex] = False  # Mark this position as False (marked).
    
    step += 1  # Increase step for the next round of marking.
    
    # Update currentIndex to be the new position in a circular way using modulo
    currentIndex = (currentIndex + step) % n  

# Step 5: Check for Unmarked Positions
unmarkedPositions = [pos for pos in marked if pos]  # Create a list of all unmarked positions.

# Step 6: Determine Output
if not unmarkedPositions:  # If there are no unmarked positions.
    print("YES")  # All positions are marked.
else:
    print("NO")  # There are still unmarked positions.

# End Program
