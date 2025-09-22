# Step 1: Accept input from the user and convert it to a positive integer
user_input = input()  # Taking input from the user
number = abs(int(user_input))  # Convert to integer and take the absolute value

# Step 2: Initialize a variable to track iterations
index = 0

# Step 3: Enter an infinite loop to find the solution
while True:
    
    # Calculate the sum of the first `index` numbers
    sum_of_numbers = (index * (index + 1)) // 2  # Using integer division

    # Calculate the difference between sum and the input number
    difference = sum_of_numbers - number

    # Step 4: Check if the sum is exactly equal to the number
    if sum_of_numbers == number:
        print(index)  # Output the current index
        break  # Exit the loop

    # Step 5: Check if the sum exceeds the input number
    elif sum_of_numbers > number:
        # Check if the difference is even
        if difference % 2 == 0:  # Checking if the difference is divisible by 2
            print(index)  # Output the current index
            break  # Exit the loop

    # Step 6: Increment the index for the next iteration
    index += 1
