def find_integer_where_sum_equals_input():
    # Prompt user for input and convert it into a positive integer
    number = int(input())
    absolute_value = abs(number)  # Get the absolute value of the input number

    # Initialize a counter variable
    index = 0  
    
    # Begin an infinite loop to search for the desired integer
    while True:
        # Calculate the sum of the first 'index' integers using the formula for the sum of a series
        sum_of_series = (index * (index + 1)) // 2
        
        # Calculate the difference between the sum and the user input
        difference = sum_of_series - absolute_value
        
        # Check if the current sum is equal to the given absolute value
        if sum_of_series == absolute_value:
            print(index)  # Print the found index
            break  # Exit the loop
        
        # Check if the current sum is greater than the absolute value of the input
        elif sum_of_series > absolute_value:
            # Check if the difference is even
            if difference % 2 == 0:
                print(index)  # Print the found index
                break  # Exit the loop
        
        # Increment the index to check the next integer
        index += 1

# To run the function, uncomment the line below
# find_integer_where_sum_equals_input()
