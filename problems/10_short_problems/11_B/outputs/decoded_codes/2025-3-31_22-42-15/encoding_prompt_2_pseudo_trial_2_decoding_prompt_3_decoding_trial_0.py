def main():
    # Step 1: Read an integer value from the user and store its absolute value as targetSum
    targetSum = abs(int(input()))

    # Step 2: Initialize the index counter
    index = 0

    # Step 3: Start an infinite loop
    while True:
        # Step 4: Calculate currentSum using the formula for the sum of the first 'index' natural numbers
        currentSum = index * (index + 1) // 2  # Integer division to get whole number
        
        # Step 5: Determine the difference between currentSum and targetSum
        difference = currentSum - targetSum
        
        # Step 6: Check for exact match
        if currentSum == targetSum:
            print(index)  # Output the value of index
            break  # Terminate loop

        # Step 7: Check for overshoot
        if currentSum > targetSum:
            # Check if the difference is even
            if difference % 2 == 0:
                print(index)  # Output the value of index
                break  # Terminate loop

        # Step 8: Increment the index
        index += 1

# End of the program. Call the main function to execute the code.
main()
