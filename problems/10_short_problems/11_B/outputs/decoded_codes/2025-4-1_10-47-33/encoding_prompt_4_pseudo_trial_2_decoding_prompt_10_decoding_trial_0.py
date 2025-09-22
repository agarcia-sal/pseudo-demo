def find_integer(n):
    # Ensure the input is a non-negative integer
    n = abs(int(n))
    
    # Initialize a counter variable to track the number of iterations
    i = 0

    # Loop indefinitely to find the integer that meets the criteria
    while True:
        # Calculate the sum of the first 'i' natural numbers
        sum_of_naturals = (i * (i + 1)) // 2  # Use integer division
        
        # Calculate the difference between the sum and the input number
        difference = sum_of_naturals - n

        # Check if the sum exactly equals the input number
        if sum_of_naturals == n:
            print(i)  # Output the current counter
            break  # Exit the loop

        # Check if the sum exceeds the input number
        elif sum_of_naturals > n:
            # Check if the difference is even
            if difference % 2 == 0:
                print(i)  # Output the current counter
                break  # Exit the loop
        
        # Increment the counter for the next iteration
        i += 1

# Read an integer input from the user
user_input = input()
find_integer(user_input)
