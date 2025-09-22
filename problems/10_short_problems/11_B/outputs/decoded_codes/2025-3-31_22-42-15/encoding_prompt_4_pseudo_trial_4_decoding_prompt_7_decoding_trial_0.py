# Begin the program

# Prompt user for input and store the absolute value of the integer
number = abs(int(input()))  # Reading an integer input and taking its absolute value

# Initialize a counter variable
index = 0

# Infinite loop to find the solution
while True:
    # Calculate the sum of the first 'index' integers
    sum_value = (index * (index + 1)) // 2  # Using integer division for accuracy

    # Calculate the difference between the sum and the input number
    difference = sum_value - number

    # Check if the sum equals the input number
    if sum_value == number:
        print(index)  # Output the index
        break  # Exit the loop

    # Check if the sum exceeds the input number
    elif sum_value > number:
        # Check if the difference is even
        if difference % 2 == 0:
            print(index)  # Output the index
            break  # Exit the loop

    # Increment the counter variable
    index += 1  # Increment index for the next iteration

# End of the program
