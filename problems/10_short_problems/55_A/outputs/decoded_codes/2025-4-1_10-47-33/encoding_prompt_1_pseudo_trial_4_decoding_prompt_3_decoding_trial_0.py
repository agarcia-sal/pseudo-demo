def process_array():
    # Step 1: Input - Read an integer n from the user
    n = int(input())
    
    # Step 2: Initialize a boolean array of size n, filled with True
    isTrue = [True] * n
    
    # Step 3: Set initial variables
    currentIndex = 0
    increment = 1
    
    # Step 4: Loop to process elements until increment exceeds 500000
    while increment <= 500000:
        if isTrue[currentIndex]:  # If the current index is still True
            isTrue[currentIndex] = False  # Mark it as processed
        
        increment += 1  # Increment the step
        currentIndex = (currentIndex + increment) % n  # Update the index with wrapping
    
    # Step 5: Check results - Collect remaining True values
    remainingTrue = [value for value in isTrue if value]  # Gather not processed values
    
    # Step 6: Output results
    if len(remainingTrue) == 0:
        print("YES")  # All elements were processed
    else:
        print("NO")   # Some elements remain True

# Execute the function
process_array()
