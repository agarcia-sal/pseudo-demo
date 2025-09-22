# Define a function to find the smallest integer based on the triangular number logic
def find_smallest_integer():
    # Step 1: Receive input
    targetNumber = abs(int(input()))  # Get the absolute value of the user's input

    # Step 2: Initialize currentInteger for evaluation
    currentInteger = 0  # Keep track of the current number being evaluated

    # Step 3: Start an infinite loop for evaluation
    while True:
        # Step 4: Calculate the triangular number using the formula
        triangularNumber = (currentInteger * (currentInteger + 1)) // 2
        
        # Step 5: Calculate the difference between triangularNumber and targetNumber
        difference = triangularNumber - targetNumber
        
        # Step 6: Check for conditions
        if triangularNumber == targetNumber:
            # Output currentInteger if triangularNumber equals targetNumber
            print(currentInteger)
            break  # Exit the loop since we found a valid number
        
        # If triangularNumber is greater than targetNumber
        elif triangularNumber > targetNumber:
            # Check if the difference is even
            if difference % 2 == 0:
                # Output currentInteger if the difference is even
                print(currentInteger)
                break  # Exit the loop since we found a valid adjustment
        
        # Step 7: Increment the integer for the next evaluation
        currentInteger += 1

# Call the function to execute the logic
find_smallest_integer()
