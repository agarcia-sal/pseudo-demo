def find_integer_sum():
    # Step 2: Declare and initialize n with the absolute value of the user input
    n = abs(int(input()))  # Assuming valid integer input from the user
    i = 0  # Step 4: Initialize the counter i to 0
    
    # Step 5: Infinite loop to find the required value
    while True:
        # Step 6: Calculate the sum of the first i natural numbers
        s = (i * (i + 1)) // 2  # using integer division
        m = s - n  # Step 7: Calculate the difference between sum and n
        
        # Step 8: Check if the sum equals n
        if s == n:
            print(i)  # Output the value of i
            break  # Step 10: Exit the loop
        
        # Step 11: Check if the sum is greater than n
        elif s > n:
            # Step 12: Check if the difference is even
            if m % 2 == 0:
                print(i)  # Output the value of i if m is even
                break  # Step 14: Exit the loop
        
        # Step 15: Increment i to check the next integer
        i += 1  # Move to the next integer

# Call the function to execute the logic
find_integer_sum()
