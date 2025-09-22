# Start of the program
# Input
n = int(input())  # Read an integer value n representing the number of elements

# Initialize the list to keep track of availability
isAvailable = [True] * n  # Create a list with n elements, all set to True
position = 0  # This will track the current index in the list
step = 1  # This represents the incrementing steps

# Loop until step exceeds 500,000
while step <= 500000:
    if isAvailable[position]:  # Check if the current position is available
        isAvailable[position] = False  # Mark this position as unavailable
    
    step += 1  # Increment the step by 1
    position = (position + step) % n  # Update the position to be within the list bounds

# Check for available positions
availablePositions = [i for i in isAvailable if i]  # Create a list of available positions

# Output Result
if len(availablePositions) == 0:  # If there are no available positions
    print("YES")  # All positions are marked as unavailable
else:
    print("NO")  # Some positions are still available
