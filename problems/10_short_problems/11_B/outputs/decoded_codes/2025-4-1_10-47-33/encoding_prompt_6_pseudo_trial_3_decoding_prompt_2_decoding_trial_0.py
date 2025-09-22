# Step 1: Accept input from the user and convert it to a positive integer
userInput = input()
number = abs(int(userInput))

# Step 2: Initialize a variable to track iterations
index = 0

# Step 3: Enter an infinite loop to find the solution
while True:
    # Calculate the sum of the first `index` numbers
    sum_value = (index * (index + 1)) // 2  # Use integer division to ensure we get an integer

    # Calculate the difference between sum and the input number
    difference = sum_value - number

    # Step 4: Check if the sum is exactly equal to the number
    if sum_value == number:
        print(index)  # Output the current index
        break  # Exit the loop

    # Step 5: Check if the sum exceeds the input number
    elif sum_value > number:

        # Check if the difference is even
        if difference % 2 == 0:
            print(index)  # Output the current index
            break  # Exit the loop

    # Step 6: Increment the index for the next iteration
    index += 1
