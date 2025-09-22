def track_positions():
    # Step 1: Input
    n = int(input())
    
    # Step 2: Initialize
    isTrue = [True] * n  # Create a list of True values of size n
    currentIndex = 0
    step = 1

    # Step 3: Loop until step exceeds 500,000
    while step <= 500000:
        if isTrue[currentIndex]:  # Check the current position
            isTrue[currentIndex] = False  # Mark it as False
        
        step += 1  # Increment step
        currentIndex = (currentIndex + step) % n  # Update currentIndex with modulo
    
    # Step 4: Filter remaining True values
    remainingTrue = [value for value in isTrue if value]

    # Step 5: Check outcome
    if len(remainingTrue) == 0:
        print("YES")  # If there are no True values left
    else:
        print("NO")   # If there are still True values left

# Call the function to execute the logic
track_positions()
