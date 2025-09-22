def find_index():
    # Read an integer input and store its absolute value
    absolute_value = abs(int(input()))

    # Initialize a counter variable 
    index = 0

    # Begin an infinite loop to find the required index
    while True:
        # Calculate the sum of the first 'index' natural numbers
        sum_natural_numbers = (index * (index + 1)) // 2
        
        # Calculate the difference between the sum and the absolute value input
        difference = sum_natural_numbers - absolute_value
        
        # Check if the sum is equal to the absolute value input
        if sum_natural_numbers == absolute_value:
            # Print the current index as the output
            print(index)
            # Exit the loop as the desired index is found
            break

        # Check if the sum is greater than the absolute value input
        elif sum_natural_numbers > absolute_value:
            # Check if the difference is even
            if difference % 2 == 0:
                # Print the current index as the output
                print(index)
                # Exit the loop as the desired index is found
                break

        # Increment the index to check the next natural number
        index += 1

# Call the function to execute
find_index()
