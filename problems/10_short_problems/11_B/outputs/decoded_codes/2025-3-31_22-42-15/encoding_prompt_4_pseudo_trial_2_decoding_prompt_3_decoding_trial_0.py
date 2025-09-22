def find_index_for_sum():
    # Step 1: Get the absolute value of an integer from user input
    number = abs(int(input()))

    index = 0  # Initialize index

    # Step 2: Infinite loop until a condition is met
    while True:
        # Calculate the sum of the first 'index' natural numbers
        sum_of_natural_numbers = (index * (index + 1)) // 2
        
        # Calculate the difference between sum and number
        difference = sum_of_natural_numbers - number
        
        # Check if the sum equals the number
        if sum_of_natural_numbers == number:
            print(index)  # Output index
            break
        
        # Check if the sum is greater than the number
        elif sum_of_natural_numbers > number:
            # Check if the difference is even
            if difference % 2 == 0:
                print(index)  # Output index
                break
        
        # Increment index for the next iteration
        index += 1

# Call the function to execute
find_index_for_sum()
