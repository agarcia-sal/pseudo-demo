def main():
    # Step 2: Input - Read an integer value n from the user
    n = int(input())
    
    # Step 3: Initialize
    isActive = [True] * n  # Create a list of size n with all elements set to True
    currentIndex = 0
    increment = 1

    # Step 4: Loop - Increment up to 500,000
    for increment in range(1, 500001):
        if isActive[currentIndex]:  # If the current element is True
            isActive[currentIndex] = False  # Set it to False
        # Update currentIndex
        currentIndex = (currentIndex + increment) % n  # Wrap around using modulo

    # Step 5: Check for Active Elements
    activeElements = [active for active in isActive if active]  # Filter to get active elements
    
    # Step 6: Output
    if len(activeElements) == 0:
        print('YES')  # All elements set to False
    else:
        print('NO')  # Some elements are still True

# Step 1: Begin Process
if __name__ == "__main__":
    main()
