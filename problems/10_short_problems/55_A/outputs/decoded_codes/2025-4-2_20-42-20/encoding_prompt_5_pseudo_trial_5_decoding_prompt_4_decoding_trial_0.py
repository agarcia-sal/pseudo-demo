def main():
    # Step 1: Get Number of Elements
    n = int(input())
    
    # Step 2: Initialize List
    isActive = [True] * n
    
    # Step 3: Set Initial Indices
    currentIndex = 0
    step = 1  # Start with step size of 1
    
    # Step 4: Process the List
    while step <= 500000:
        if isActive[currentIndex]:  # Check if current element is True
            isActive[currentIndex] = False  # Mark as inactive
        
        step += 1  # Increment step for the next iteration
        currentIndex = (currentIndex + step) % n  # Wrap around using modulo to stay within bounds
    
    # Step 5: Check Remaining Active Elements
    remainingActive = [active for active in isActive if active]
    
    # Step 6: Output Result
    if len(remainingActive) == 0:
        print("YES")
    else:
        print("NO")

# Running the main function
if __name__ == "__main__":
    main()
