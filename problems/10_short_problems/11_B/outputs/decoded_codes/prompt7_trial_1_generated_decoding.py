def find_matching_integer_from_sum_of_integers():
    # Prompt user for input and convert to absolute integer
    user_input = abs(int(input()))

    # Initialize counter variable
    index = 0
    
    # Infinite loop until a break occurs
    while True:
        # Calculate the sum of first 'index' integers using the formula n(n+1)/2
        sum_of_integers = (index * (index + 1)) // 2
        
        # Calculate the difference between the calculated sum and user input
        difference = sum_of_integers - user_input
        
        # Check if the calculated sum equals user input
        if sum_of_integers == user_input:
            print(index)
            break
        
        # Check if the calculated sum is greater than user input
        elif sum_of_integers > user_input:
            # Check if the difference is even
            if difference % 2 == 0:
                print(index)
                break
        
        # Increment the counter for the next iteration
        index += 1

# Invoke the function to execute
find_matching_integer_from_sum_of_integers()
