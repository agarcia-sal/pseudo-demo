# Function to determine if all positions in the list can be marked inactive
def check_all_positions_inactive():
    # Read the size of the list
    n = int(input())
    
    # Initialize the list with all elements set to True (active)
    isActive = [True] * n
    
    # Set initial counters
    currentPosition = 0
    stepCount = 1
    
    # Loop until stepCount exceeds 500,000
    while stepCount <= 500000:
        # Mark the current position as inactive if active
        if isActive[currentPosition]:
            isActive[currentPosition] = False
        
        # Increment step count and calculate new position
        stepCount += 1
        currentPosition = (currentPosition + stepCount) % n  # Wrap around using modulo
    
    # Identify all positions that remain active
    inactivePositions = [index for index, active in enumerate(isActive) if active]
    
    # Output result based on the status of inactivePositions
    if not inactivePositions:  # If no positions are active
        print("YES")  # All positions got marked inactive
    else:
        print("NO")   # At least one position remains active

# Optionally, invoke the function to test
# check_all_positions_inactive() 
