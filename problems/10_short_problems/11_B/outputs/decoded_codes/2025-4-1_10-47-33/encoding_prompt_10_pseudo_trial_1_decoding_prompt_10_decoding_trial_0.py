def find_natural_number(n):
    # Step 1: Get the absolute integer value of user input
    n = abs(n)
    
    # Step 2: Initialize the counter variable i
    i = 0

    # Step 3: Begin an infinite loop to find the result
    while True:
        # Calculate the sum of the first i natural numbers
        s = (i * (i + 1)) // 2  # Using integer division to keep the result an integer
        
        # Calculate the difference between sum and input
        m = s - n
        
        # Step 4: Check if the sum s equals n
        if s == n:
            print(i)  # Output the result
            break
        
        # Step 5: Check if the sum s exceeds n
        elif s > n:
            # Step 6: Check if the difference m is even
            if m % 2 == 0:
                print(i)  # Output the result
                break
        
        # Increment the counter for the next iteration
        i += 1

# Getting user input
user_input = int(input())  # Step 1 input, assuming valid integer input
find_natural_number(user_input)
