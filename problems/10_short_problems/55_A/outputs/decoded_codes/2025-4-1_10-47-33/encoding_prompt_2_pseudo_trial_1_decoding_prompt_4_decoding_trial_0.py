def main():
    # Step 1: Initialize Input
    numberOfElements = int(input())
    
    # Step 2: Create a Boolean List
    isActive = [True] * numberOfElements  # Initialize list with True values
    
    # Step 3: Set Initial Indices
    currentIndex = 0  # Current position in isActive list
    stepSize = 1  # Initial step size for elimination process
    
    # Step 4: Start Elimination Process
    while stepSize <= 500000:
        if isActive[currentIndex]:  # Check if the current position is active
            isActive[currentIndex] = False  # Mark this position as inactive
            
        stepSize += 1  # Increment step size
        currentIndex = (currentIndex + stepSize) % numberOfElements  # Update the current index
    
    # Step 5: Check Remaining Active Entries
    remainingActive = [active for active in isActive if active]  # List of still active positions
    
    # Step 6: Determine and Print Final Result
    if len(remainingActive) == 0:
        print("YES")  # All positions have been eliminated
    else:
        print("NO")  # Some positions are still active

# Invoke the main function to run the code
if __name__ == "__main__":
    main()
