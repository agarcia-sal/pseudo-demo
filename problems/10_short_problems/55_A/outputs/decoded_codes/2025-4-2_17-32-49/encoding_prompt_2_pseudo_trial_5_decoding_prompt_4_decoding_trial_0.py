def main():
    # Step 2: Input Requirement
    totalElements = int(input())

    # Step 3: Initialize
    isActive = [True] * totalElements  # List of active elements, initialized to True
    index = 0  # Current index tracker
    step = 1   # Step variable
    
    # Step 4: Loop to mark elements inactive
    while step <= 500000:
        if isActive[index]:  # Check if the current element is active
            isActive[index] = False  # Mark as inactive
        step += 1  # Increase the step
        index = (index + step) % totalElements  # Update index with wrap-around
    
    # Step 5: Filter Active Elements
    activeElements = [element for element in isActive if element]
    
    # Step 6: Output Requirement
    if len(activeElements) == 0:
        print("YES")  # All elements are inactive
    else:
        print("NO")   # Some elements remain active

# Step 1: Start
if __name__ == "__main__":
    main()
