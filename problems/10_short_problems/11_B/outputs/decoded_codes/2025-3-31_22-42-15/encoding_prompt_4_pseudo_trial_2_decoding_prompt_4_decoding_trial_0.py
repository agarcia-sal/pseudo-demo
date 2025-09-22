def find_index_for_sum():
    # Get the absolute value of an integer from user input
    number = abs(int(input()))
    
    index = 0
    
    # Infinite loop until a condition is met
    while True:
        # Calculate the sum of the first 'index' natural numbers
        sum_index = (index * (index + 1)) // 2
        
        # Calculate the difference between sum and number
        difference = sum_index - number
        
        # Check if the sum equals the number
        if sum_index == number:
            print(index)
            break
            
        # Check if the sum is greater than the number
        elif sum_index > number:
            # Check if the difference is even
            if difference % 2 == 0:
                print(index)
                break
        
        # Increment index for the next iteration
        index += 1

# Call the function to execute the code
find_index_for_sum()
