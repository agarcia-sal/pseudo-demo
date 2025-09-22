def find_integer():
    # Convert input to a non-negative integer
    n = abs(int(input()))  # Read input and take the absolute value

    i = 0  # Initialize index i to 0

    # Begin an infinite loop to find the result
    while True:
        # Calculate the sum of the first i integers
        s = (i * (i + 1)) // 2
        
        # Calculate the difference between the sum and the target number
        m = s - n
        
        # Check if the current sum equals the target number
        if s == n:
            print(i)  # Print index i
            break  # Exit the loop
        
        # Check if the current sum exceeds the target number
        elif s > n:
            # Check if the difference is even
            if m % 2 == 0:
                print(i)  # Print index i
                break  # Exit the loop
        
        # Increment index i for the next iteration
        i += 1

# Call the function to execute
find_integer()
