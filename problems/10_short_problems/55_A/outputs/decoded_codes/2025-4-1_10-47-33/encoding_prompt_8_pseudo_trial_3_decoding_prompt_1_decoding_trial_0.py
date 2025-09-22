# Begin Program

# Get Input:
n = int(input())  # Read a number 'n' which represents the number of positions in a list.

# Initialize List:
marked = [True] * n  # Create a list 'marked' of size 'n' filled with 'True'.

# Set Initial Variables:
currentIndex = 0  # This will track the current position.
step = 1          # This will determine the step size for marking.

# Mark Unmarked Positions:
while step <= 500000:  # While step is less than or equal to 500,000
    if marked[currentIndex]:  # Check if the position at currentIndex is True
        marked[currentIndex] = False  # Mark this position as False

    step += 1  # Increase step by 1

    # Update currentIndex to be the new position
    currentIndex = (currentIndex + step) % n  # Wrap around using modulo

# Check for Unmarked Positions:
unmarkedPositions = [position for position in marked if position]  # Create a list of unmarked positions

# Determine Output:
if not unmarkedPositions:  # If the list of unmarked positions is empty
    print("YES")  # Indicating all positions were marked
else:
    print("NO")  # Indicating there are still unmarked positions

# End Program
