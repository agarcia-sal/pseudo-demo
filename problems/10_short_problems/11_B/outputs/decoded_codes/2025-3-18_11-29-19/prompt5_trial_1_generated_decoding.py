def find_smallest_integer():
    # Step 1: Accept absolute value input from the user
    number = abs(int(input()))

    # Step 2: Initialize a counter variable
    index = 0

    # Step 3: Infinite loop to find the required integer
    while True:
        # Calculate the sum of the first 'index' integers
        sum_first_index = index * (index + 1) // 2  # Using the formula for sum of first n integers

        # Calculate the difference between the sum and the input number
        difference = sum_first_index - number

        # Step 4: Check if the sum matches the input number
        if sum_first_index == number:
            print(index)  # Output the current index
            break  # Stop the loop as we found the solution
        
        # Step 5: Check if the sum exceeds the input number
        elif sum_first_index > number:
            # Check if the difference is even
            if difference % 2 == 0:
                print(index)  # Output the current index
                break  # Stop the loop as we found the solution
        
        # Step 6: Increment the counter to check the next integer
        index += 1  # Move to the next integer

# To run the function
find_smallest_integer()
