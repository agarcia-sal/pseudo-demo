def find_index_for_sum_of_natural_numbers():
    # Get the absolute value of an integer from user input
    number = abs(int(input()))
    
    index = 0  # Initialize the index
    
    # Infinite loop until a condition is met
    while True:
        # Calculate the sum of the first 'index' natural numbers
        sum_of_natural_numbers = (index * (index + 1)) // 2
        
        # Calculate the difference between sum and number
        difference = sum_of_natural_numbers - number
        
        # Check if the sum equals the number
        if sum_of_natural_numbers == number:
            print(index)
            break
        
        # Check if the sum is greater than the number
        elif sum_of_natural_numbers > number:
            # Check if the difference is even
            if difference % 2 == 0:
                print(index)
                break
        
        # Increment index for the next iteration
        index += 1


# Function to run the main logic
if __name__ == "__main__":
    find_index_for_sum_of_natural_numbers()
