# Begin Program

# Get Input
n = int(input())  # Read a number 'n' that represents the number of positions in a list

# Initialize List
marked = [True] * n  # Create a list 'marked' of size 'n' filled with 'True'

# Set Initial Variables
currentIndex = 0  # This will track the current position
step = 1          # This will determine the step size for marking

# Mark Unmarked Positions
while step <= 500000:  # While 'step' is less than or equal to 500,000
    if marked[currentIndex]:  # Check if the position at 'currentIndex' in 'marked' list is True
        marked[currentIndex] = False  # Change the value to 'False' indicating this position is now marked
    
    step += 1  # Increase 'step' by 1 to prepare for the next round of marking
    currentIndex = (currentIndex + step) % n  # Update 'currentIndex' circularly

# Check for Unmarked Positions
unmarkedPositions = [pos for pos in marked if pos]  # List of all 'True' values in 'marked'

# Determine Output
if not unmarkedPositions:  # If 'unmarkedPositions' is empty
    print("YES")  # All positions were marked
else:
    print("NO")  # There are still unmarked positions

# End Program
