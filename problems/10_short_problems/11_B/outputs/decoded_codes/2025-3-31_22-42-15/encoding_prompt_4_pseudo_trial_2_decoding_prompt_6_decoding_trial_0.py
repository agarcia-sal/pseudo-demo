# Begin the program

# Get the absolute value of an integer from user input
number = abs(int(input()))  # Convert input to integer and get its absolute value

index = 0  # Initialize index to 0

# Infinite loop until a condition is met
while True:
    # Calculate the sum of the first 'index' natural numbers
    sum_value = (index * (index + 1)) // 2  # Use integer division for the sum

    # Calculate the difference between sum and number
    difference = sum_value - number

    # Check if the sum equals the number
    if sum_value == number:
        print(index)  # Output the index
        break  # Exit the loop
    
    # Check if the sum is greater than the number
    elif sum_value > number:
        # Check if the difference is even
        if difference % 2 == 0:  # Check if the difference is even
            print(index)  # Output the index
            break  # Exit the loop
    
    # Increment index for the next iteration
    index += 1  # Increase index by 1

# End of the program
