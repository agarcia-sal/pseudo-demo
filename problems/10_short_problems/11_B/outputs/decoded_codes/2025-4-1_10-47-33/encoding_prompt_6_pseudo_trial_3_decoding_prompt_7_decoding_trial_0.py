# Step 1: Accept input from the user and convert it to a positive integer
userInput = input()  # Get user input as a string
number = abs(int(userInput))  # Convert to integer and take absolute value

# Step 2: Initialize a variable to track iterations
index = 0

# Step 3: Enter an infinite loop to find the solution
while True:
    # Calculate the sum of the first `index` numbers using the arithmetic series formula
    sum = (index * (index + 1)) // 2  # Use integer division

    # Calculate the difference between sum and the input number
    difference = sum - number

    # Step 4: Check if the sum is exactly equal to the number
    if sum == number:
        print(index)  # Output the current index
        break  # Exit the loop
    
    # Step 5: Check if the sum exceeds the input number
    elif sum > number:
        # Check if the difference is even
        if difference % 2 == 0:
            print(index)  # Output the current index
            break  # Exit the loop

    # Step 6: Increment the index for the next iteration
    index += 1  # Increase the index for the next check
