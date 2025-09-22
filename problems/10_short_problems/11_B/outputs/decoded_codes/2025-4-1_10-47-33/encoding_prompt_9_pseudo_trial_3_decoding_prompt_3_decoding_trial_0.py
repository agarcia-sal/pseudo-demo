# Function to find the smallest non-negative integer
def find_smallest_integer():
    # Step 1: Receive Input
    targetValue = abs(int(input()))  # Convert input to absolute integer

    # Step 2: Initialize Variables
    index = 0  # Counter for the current integer

    # Step 3: Infinite Loop
    while True:
        # Step 1.1: Calculate Sum
        currentSum = (index * (index + 1)) // 2  # Calculate the sum up to index
        
        # Step 1.2: Calculate Difference
        diff = currentSum - targetValue
        
        # Step 1.3: Check for Equality
        if currentSum == targetValue:
            # Output the value of index
            print(index)
            break  # Exit the loop
        
        # Step 1.4: Check for Greater Sum
        if currentSum > targetValue:
            if diff % 2 == 0:  # Check if the remainder is even
                # Output the value of index
                print(index)
                break  # Exit the loop
        
        # Step 1.5: Increment Index
        index += 1  # Move to the next integer

# Call the function to execute
find_smallest_integer()
