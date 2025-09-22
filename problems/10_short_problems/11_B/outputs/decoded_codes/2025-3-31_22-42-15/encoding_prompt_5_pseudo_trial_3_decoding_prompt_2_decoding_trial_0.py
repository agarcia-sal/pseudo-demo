# Step 1: Get user input and ensure it is a non-negative integer
userInput = abs(int(input()))  # Read an absolute value of integer from user
counter = 0

# Step 2: Start an infinite loop to iterate through possible values
while True:
    
    # Step 3: Calculate the current triangular number
    currentTriangularNumber = (counter * (counter + 1)) // 2
    
    # Step 4: Determine the difference between the triangular number and user input
    difference = currentTriangularNumber - userInput
    
    # Step 5: Check conditions to decide what to do next
    if currentTriangularNumber == userInput:
        # If the triangular number equals user input, print the counter and stop
        print(counter)
        break
    
    elif currentTriangularNumber > userInput:
        # If the triangular number exceeds user input, check if difference is even
        if difference % 2 == 0:
            # If the difference is even, print the counter and stop
            print(counter)
            break

    # Step 6: Increment the counter for the next iteration
    counter += 1
