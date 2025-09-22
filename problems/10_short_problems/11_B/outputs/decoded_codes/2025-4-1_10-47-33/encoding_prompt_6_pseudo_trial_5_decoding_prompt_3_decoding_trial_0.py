def main():
    # Get the absolute value of user input as an integer
    number = abs(int(input()))

    # Initialize a variable to keep track of index
    index = 0

    # Start an infinite loop to process the logic
    while True:
        # Calculate the sum of the first 'index' natural numbers
        sum_natural_numbers = (index * (index + 1)) // 2  # Using integer division
        
        # Calculate the difference between the sum and the input number
        difference = sum_natural_numbers - number
        
        # Check if the calculated sum matches the input number
        if sum_natural_numbers == number:
            print(index)
            break
        
        # Check if the sum has exceeded the input number
        elif sum_natural_numbers > number:
            
            # Check if the difference is even
            if difference % 2 == 0:
                print(index)
                break
        
        # Increment the index for the next iteration
        index += 1

# Call the main function
main()
