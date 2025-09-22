def find_integer():
    # Read integer input and take the absolute value
    n = abs(int(input()))
    
    # Initialize the counter variable
    i = 0
    
    # Loop indefinitely until the conditions are met
    while True:
        # Calculate the sum of the first i integers using the formula (i * (i + 1)) / 2
        sum_of_integers = (i * (i + 1)) // 2
        
        # Calculate the difference between the current sum and n
        difference = sum_of_integers - n
        
        # Check if we found the exact sum equal to n
        if sum_of_integers == n:
            print(i)  # Output the current value of i
            return  # Terminate the function

        # Check if the sum is greater than n
        elif sum_of_integers > n:
            # If the difference is even, we have found our result
            if difference % 2 == 0:
                print(i)  # Output the current value of i
                return  # Terminate the function
        
        # Increment i for the next iteration
        i += 1

# Call the function to execute
find_integer()
