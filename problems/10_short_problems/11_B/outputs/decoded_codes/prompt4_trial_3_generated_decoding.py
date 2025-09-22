def find_sum_index():
    # Read an integer input and take the absolute value
    n = abs(int(input()))

    # Initialize a variable to keep track of the current index
    i = 0

    # Infinite loop to find the desired index
    while True:
        # Calculate the sum of the first i natural numbers
        s = (i * (i + 1)) // 2  # Using integer division
        
        # Compute the difference between the sum and n
        m = s - n
        
        # Check if the sum is equal to n
        if s == n:
            print(i)
            break
        
        # Check if the sum exceeds n
        elif s > n:
            # Check if the difference is even
            if m % 2 == 0:
                print(i)
                break
        
        # Increment the index
        i += 1

# Call the function to execute
find_sum_index()
