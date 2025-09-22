def find_index_for_number():
    # Read an integer input value and store its absolute value in 'number'
    number = abs(int(input()))
    
    index = 0  # Initialize index to 0
    
    while True:  # Start an infinite loop
        # Calculate the sum of the first 'index' natural numbers
        sum_of_first_index = (index * (index + 1)) / 2
        
        # Calculate the difference between sum_of_first_index and number
        difference = sum_of_first_index - number
        
        # Check if sum_of_first_index is equal to number
        if sum_of_first_index == number:
            print(index)  # Print the value of index and exit the loop
            break
        
        # Check if sum_of_first_index is greater than number
        elif sum_of_first_index > number:
            # Check if difference is even
            if difference % 2 == 0:
                print(index)  # Print the value of index and exit the loop
                break
        
        # Increment index by 1 for the next iteration
        index += 1

# Call the function to execute
find_index_for_number()
