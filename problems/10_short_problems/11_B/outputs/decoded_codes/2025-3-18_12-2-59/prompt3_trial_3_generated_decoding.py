def find_index_for_sum():
    # Step 1: Get the absolute integer input
    number = abs(int(input()))  # Getting absolute value of user input
    
    # Step 2: Initialize index variable
    index = 0

    # Step 3: Start an infinite loop to find the desired result
    while True:
        # Calculate the sum of the first 'index' natural numbers
        sum_natural_numbers = (index * (index + 1)) // 2
        
        # Calculate the difference between sum and input number
        difference = sum_natural_numbers - number
        
        # Step 4: Check if the sum equals the input number
        if sum_natural_numbers == number:
            print(index)  # Output the current index
            break  # Exit the loop
        
        # Step 5: Check if sum exceeds the input number
        elif sum_natural_numbers > number:
            # Check if the difference is even
            if difference % 2 == 0:
                print(index)  # Output the current index
                break  # Exit the loop
        
        # Step 6: Increment index for the next iteration
        index += 1

# Example execution
find_index_for_sum()
