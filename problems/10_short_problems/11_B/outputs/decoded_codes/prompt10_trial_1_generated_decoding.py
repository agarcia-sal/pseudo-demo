def find_natural_number():
    # Get the absolute integer input from the user
    n = abs(int(input()))
    i = 0

    # Infinite loop
    while True:
        # Calculate the sum of the first i natural numbers
        s = (i * (i + 1)) // 2  # Using integer division to avoid floating-point results
        
        # Calculate the difference between the sum and n
        m = s - n
        
        # Check if the sum equals n
        if s == n:
            print(i)
            break

        # Check if the sum is greater than n
        elif s > n:
            # Check if the difference is even
            if m % 2 == 0:
                print(i)
                break
            
        # Increment i for the next iteration
        i += 1

# Call the function to execute the program
find_natural_number()
