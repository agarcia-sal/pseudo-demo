def find_natural_number():
    # Read and convert input to an absolute integer
    number = abs(int(input()))
    
    # Initialize index variable
    index = 0

    # Infinite loop to find the solution
    while True:
        # Calculate the sum of first 'index' natural numbers
        total_sum = (index * (index + 1)) // 2
        
        # Calculate the difference between sum and number
        difference = total_sum - number
        
        # Check if the sum equals the number
        if total_sum == number:
            print(index)
            break
        
        # Check if the sum is greater than the number
        elif total_sum > number:
            # Check if the difference is even
            if difference % 2 == 0:
                print(index)
                break
        
        # Increment the index for the next iteration
        index += 1

# Call the function to execute the logic
find_natural_number()
