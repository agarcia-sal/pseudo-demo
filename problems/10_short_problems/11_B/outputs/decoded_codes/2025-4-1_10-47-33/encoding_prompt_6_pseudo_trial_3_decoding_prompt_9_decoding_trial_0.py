# Accept input from the user and convert it to a positive integer
user_input = input()
number = abs(int(user_input))

# Initialize a variable to track iterations
index = 0

# Enter an infinite loop to find the solution
while True:
    # Calculate the sum of the first `index` numbers
    sum_value = (index * (index + 1)) // 2
    
    # Calculate the difference between sum and the input number
    difference = sum_value - number

    # Check if the sum is exactly equal to the number
    if sum_value == number:
        print(index)  # Output the current index
        break  # Exit the loop
    
    # Check if the sum exceeds the input number
    elif sum_value > number:
        # Check if the difference is even
        if difference % 2 == 0:
            print(index)  # Output the current index
            break  # Exit the loop

    # Increment the index for the next iteration
    index += 1
