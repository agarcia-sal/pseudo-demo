# Start the program.

# Input the total number of elements:
totalElements = int(input())

# Initialize a list of boolean values:
isActive = [True] * totalElements  # Create a list filled with True

# Set up counters:
currentIndex = 0  # Initialize the position tracker
step = 1          # Define the step size

# Loop for a maximum of 500,000 iterations:
while step <= 500000:
    if isActive[currentIndex]:  # Check if the current position is still active
        isActive[currentIndex] = False  # Mark it as inactive
    step += 1  # Increment step
    currentIndex = (currentIndex + step) % totalElements  # Update position with wrap-around

# Collect remaining active elements:
remainingActive = [index for index, value in enumerate(isActive) if value]  # Get all active indices

# Check the result:
if len(remainingActive) == 0:  # If there are no active elements left
    print("YES")  # Output YES
else:
    print("NO")   # Output NO

# End the program.
