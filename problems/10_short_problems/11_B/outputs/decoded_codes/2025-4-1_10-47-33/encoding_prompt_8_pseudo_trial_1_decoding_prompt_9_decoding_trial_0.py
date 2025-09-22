# Get Input
targetNumber = int(input())  # Convert input to a non-negative integer

# Ensure targetNumber is non-negative
if targetNumber < 0:
    print("Please enter a non-negative integer.")
else:
    # Initialize Variables
    currentInteger = 0
    
    # Loop to Find the Result
    while True:  # Start an endless loop
        # Calculate the sum of all integers from 0 to currentInteger
        sumOfIntegers = (currentInteger * (currentInteger + 1)) // 2  # Using formula for sum of first n integers
        
        # Calculate the difference
        difference = sumOfIntegers - targetNumber
        
        # Check Conditions
        if sumOfIntegers == targetNumber:
            print(currentInteger)  # Print the solution
            break  # Exit the loop
        elif sumOfIntegers > targetNumber:
            if difference % 2 == 0:  # Check if the difference is even
                print(currentInteger)  # Print the solution
                break  # Exit the loop
        
        # Increase currentInteger to consider the next integer in the next iteration
        currentInteger += 1
