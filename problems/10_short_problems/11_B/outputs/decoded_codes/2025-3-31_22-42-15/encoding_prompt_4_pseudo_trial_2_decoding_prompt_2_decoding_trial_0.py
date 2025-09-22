# Get the absolute value of an integer from user input
number = abs(int(input()))

index = 0

# Infinite loop until a condition is met
while True:
    # Calculate the sum of the first 'index' natural numbers
    sum_value = (index * (index + 1)) // 2  # Using integer division

    # Calculate the difference between sum and number
    difference = sum_value - number

    # Check if the sum equals the number
    if sum_value == number:
        print(index)  # OUTPUT index
        break

    # Check if the sum is greater than the number
    elif sum_value > number:
        # Check if the difference is even
        if difference % 2 == 0:
            print(index)  # OUTPUT index
            break

    # Increment index for the next iteration
    index += 1
