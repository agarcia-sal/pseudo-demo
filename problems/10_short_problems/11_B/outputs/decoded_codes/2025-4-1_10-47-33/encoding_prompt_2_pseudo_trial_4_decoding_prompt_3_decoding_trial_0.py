# Function to find the current index that matches the target sum condition
def find_target_index():
    # Step 2: Read input from the user and store the absolute value in targetSum
    targetSum = abs(int(input()))
    
    # Step 3: Initialize currentIndex to 0
    currentIndex = 0
    
    # Step 4: Begin an infinite loop
    while True:
        # Step 4.1: Calculate the sum of the first currentIndex integers
        currentSum = (currentIndex * (currentIndex + 1)) // 2
        
        # Step 4.2: Calculate the difference from targetSum
        differenceFromTarget = currentSum - targetSum
        
        # Step 4.3: Check for exact match
        if currentSum == targetSum:
            print(currentIndex)  # Output the index
            break  # Exit the loop
        
        # Step 4.4: Check if currentSum exceeds targetSum
        if currentSum > targetSum:
            # If the difference is even, output the index and exit the loop
            if differenceFromTarget % 2 == 0:
                print(currentIndex)  # Output the index
                break  # Exit the loop
        
        # Step 4.5: Increment currentIndex by 1
        currentIndex += 1

# Test the function
find_target_index()
