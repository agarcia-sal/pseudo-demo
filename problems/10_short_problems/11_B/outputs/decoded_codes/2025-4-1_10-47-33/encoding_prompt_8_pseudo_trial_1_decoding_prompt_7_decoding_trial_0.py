# Function to find the smallest non-negative integer whose sum of integers up to it
# can equal a given target number or an even adjustment of it.
def find_small_integer():
    # Step 1: Get Input
    targetNumber = int(input())  # Read input and convert to integer
    
    # Step 2: Initialize Variables
    currentInteger = 0  # Start from 0
    
    # Step 3: Loop to Find the Result
    while True:  # Endless loop until we break out of it
        # Calculate sum of all integers from 0 to currentInteger
        sumOfIntegers = (currentInteger * (currentInteger + 1)) // 2  # Using the formula n(n+1)/2
        
        # Calculate the difference from the targetNumber
        difference = sumOfIntegers - targetNumber
        
        # Check Conditions
        if sumOfIntegers == targetNumber:  # Case 1: Exact match
            print(currentInteger)  # Print the solution
            break  # Exit the loop
        elif sumOfIntegers > targetNumber:  # Case 2: Sum exceeded targetNumber
            if difference % 2 == 0:  # Check if difference is even
                print(currentInteger)  # Print the solution
                break  # Exit the loop
        
        # Increment currentInteger for next iteration
        currentInteger += 1

# Call the function to execute
find_small_integer()
