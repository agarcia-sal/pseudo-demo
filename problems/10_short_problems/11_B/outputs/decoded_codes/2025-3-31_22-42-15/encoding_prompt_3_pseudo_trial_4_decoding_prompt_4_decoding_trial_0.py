def find_index_of_natural_sum():
    # Input: Receive an integer input and take its absolute value
    input_number = abs(int(input()))

    # Initialize a variable to track iterative counting
    index = 0

    # Start an infinite loop to find the solution
    while True:
        # Calculate the sum of the first 'index' natural numbers
        sum_to_index = (index * (index + 1)) // 2
        
        # Determine the difference from the target input
        difference = sum_to_index - input_number

        # Check if the current sum equals the target input
        if sum_to_index == input_number:
            # Output the current index which is the result
            print(index)
            break
        
        # Check if the current sum exceeds the target input
        elif sum_to_index > input_number:
            # Check if the difference is even
            if difference % 2 == 0:
                # Output the current index which is the result
                print(index)
                break
        
        # Increment the index to check the next natural number
        index += 1

# Call the function to execute the program
find_index_of_natural_sum()
