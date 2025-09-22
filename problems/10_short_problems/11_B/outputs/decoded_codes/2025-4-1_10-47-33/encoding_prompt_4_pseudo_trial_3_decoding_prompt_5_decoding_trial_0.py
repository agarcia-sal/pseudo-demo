def find_natural_number():
    # Read and convert input to an absolute integer
    number = abs(int(input()))

    # Initialize index variable
    index = 0

    # Infinite loop to find the solution
    while True:
        # Calculate the sum of first 'index' natural numbers
        sum_of_naturals = (index * (index + 1)) // 2
        
        # Calculate the difference between sum and number
        difference = sum_of_naturals - number
        
        # Check if the sum equals the number
        if sum_of_naturals == number:
            print(index)
            break
            
        # Check if the sum is greater than the number
        elif sum_of_naturals > number:
            # Check if the difference is even
            if difference % 2 == 0:
                print(index)
                break
            
        # Increment the index for the next iteration
        index += 1

# Example usage (uncomment for testing):
# find_natural_number()
