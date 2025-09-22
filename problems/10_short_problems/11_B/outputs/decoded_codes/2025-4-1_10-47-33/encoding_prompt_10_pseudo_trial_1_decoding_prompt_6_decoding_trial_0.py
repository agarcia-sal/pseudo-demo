# Start of the program

# Step 1: Get the absolute integer input
n = abs(int(input()))  # Read input, convert to integer, and take absolute value

# Step 2: Initialize the counter variable
i = 0  # This variable will be used to count up from 0

# Step 3: Begin an infinite loop to find the result
while True:
    # Step 4: Calculate the sum of the first i natural numbers
    sum_of_natural_numbers = (i * (i + 1)) / 2  # Formula for sum of first i natural numbers
    
    # Step 5: Calculate the difference between sum and input
    difference = sum_of_natural_numbers - n  # Calculate the difference
    
    # Check if the sum equals n
    if sum_of_natural_numbers == n:
        print(i)  # Print the value of i if the sum equals n
        break  # Exit the loop
        
    # Check if the sum exceeds n
    elif sum_of_natural_numbers > n:
        # Step 6: Check if the difference is even
        if difference % 2 == 0:  # Use modulo to check if the difference is even
            print(i)  # Print the value of i if the difference is even
            break  # Exit the loop
    
    # Increment the counter for the next iteration
    i += 1  # Increase i by 1 for the next iteration
