def main():
    # Step 1: Get Input
    n = int(input())  # Read the integer input for the size of the list
    
    # Step 2: Initialize List
    isActive = [True] * n  # Create a list with n elements all set to True
    
    # Step 3: Initialize Counters
    currentIndex = 0
    stepNumber = 1
    
    # Step 4: Iterate to Modify List
    while stepNumber <= 500000:
        if isActive[currentIndex]:  # If the current position is True
            isActive[currentIndex] = False  # Mark it as inactive (False)
        
        # Increase stepNumber and calculate the new index
        stepNumber += 1
        currentIndex = (currentIndex + stepNumber) % n  # Update index with wrap-around
        
    # Step 5: Check Remaining Active Elements
    remainingActive = [value for value in isActive if value]  # List of True values
    
    # Step 6: Determine Output
    if len(remainingActive) == 0:  # If no True values are left
        print("YES")  # All elements are inactive
    else:
        print("NO")  # At least one element is still active

# Call the main function to execute the code
if __name__ == "__main__":
    main()
