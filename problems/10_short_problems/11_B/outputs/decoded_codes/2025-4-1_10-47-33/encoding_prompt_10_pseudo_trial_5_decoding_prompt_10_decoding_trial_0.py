def find_integer_sum():
    # Get absolute integer input from user
    n = abs(int(input()))

    i = 0  # Initialize i to 0

    while True:
        # Calculate the sum of the first i integers
        s = (i * (i + 1)) // 2
        m = s - n  # Calculate the difference between sum and n

        if s == n:  # Check if the sum equals n
            print(i)  # Output the value of i
            break  # Exit the loop
        
        elif s > n:  # Check if the sum exceeds n
            if m % 2 == 0:  # Check if the difference is even
                print(i)  # Output the value of i
                break  # Exit the loop
        
        i += 1  # Increment i by 1

# Call the function to execute it
find_integer_sum()
