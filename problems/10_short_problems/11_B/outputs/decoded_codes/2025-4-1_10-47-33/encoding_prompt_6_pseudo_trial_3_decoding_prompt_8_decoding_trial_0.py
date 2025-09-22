# Step 1: Accept input from the user and convert it to a positive integer
userInput = input()
number = abs(int(userInput))

# Step 2: Initialize a variable to track iterations
index = 0

# Step 3: Enter an infinite loop to find the solution
while True:
    # Calculate the sum of the first `index` numbers
    sum = (index * (index + 1)) // 2
    
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
    index += 1
