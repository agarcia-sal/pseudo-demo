# Begin Program

# Get Input
n = int(input())  # Read a number which represents the number of positions in a list.

# Initialize List
marked = [True] * n  # Create a list filled with True, indicating all positions are initially unmarked.

# Set Initial Variables
currentIndex = 0  # This will track the current position.
step = 1  # This will determine the step size for marking.

# Mark Unmarked Positions
while step <= 500000:  # Continue marking until the step limit is reached
    if marked[currentIndex]:  # Check if the current position is unmarked
        marked[currentIndex] = False  # Mark the position as False (now marked)
    
    step += 1  # Increase step to prepare for the next marking
    currentIndex = (currentIndex + step) % n  # Update currentIndex circularly

# Check for Unmarked Positions
unmarkedPositions = [pos for pos in marked if pos]  # Collect all unmarked positions

# Determine Output
if not unmarkedPositions:  # If there are no unmarked positions
    print("YES")  # All positions were marked
else:
    print("NO")  # There are still unmarked positions

# End Program
