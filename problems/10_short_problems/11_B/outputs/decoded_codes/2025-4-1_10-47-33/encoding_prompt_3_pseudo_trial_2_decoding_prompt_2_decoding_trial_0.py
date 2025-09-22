# Step 1: Read user input and prepare the variable
userInput = abs(int(input()))  # This will be the target number (n)

# Step 2: Initialize the variable for loop control
index = 0

# Step 3: Use an indefinite loop to find the solution
while True:
    
    # Step 4: Calculate the sum of the first 'index' integers
    sum = (index * (index + 1)) // 2  # Use integer division to maintain whole numbers
    
    # Step 5: Calculate the difference between the sum and user input
    difference = sum - userInput
    
    # Step 6: Check if the sum matches the user input
    if sum == userInput:
        print(index)  # Output the index if it's a match
        break  # Exit the loop

    # Step 7: Check if the sum exceeds the user input
    elif sum > userInput:
        # Step 8: Check if the difference is even
        if difference % 2 == 0:  # Check if the difference is even
            print(index)  # Output the index if the condition is met
            break  # Exit the loop

    # Step 9: Increment the index to try the next integer
    index += 1
