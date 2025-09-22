def findSmallestInteger():
    # Read user input and convert to absolute integer value
    n = abs(int(input()))
    
    # Initialize the counter variable 'i'
    i = 0

    # Infinite loop to find the smallest integer
    while True:
        # Calculate the sum of the first 'i' integers using the formula
        s = (i * (i + 1)) // 2
        
        # Calculate the difference between the sum and 'n'
        m = s - n

        # Check if the sum is equal to 'n'
        if s == n:
            print(i)  # Print the result
            break  # Exit the loop
        
        # Check if the sum is greater than 'n'
        elif s > n:
            # Check if the difference 'm' is even
            if m % 2 == 0:
                print(i)  # Print the result
                break  # Exit the loop
        
        # Increment 'i' for the next iteration
        i += 1

# Call the function to execute
findSmallestInteger()
