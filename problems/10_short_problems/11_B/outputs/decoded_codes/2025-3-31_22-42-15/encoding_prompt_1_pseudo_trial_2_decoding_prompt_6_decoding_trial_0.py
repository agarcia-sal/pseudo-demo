# Step 1: Start the program

# Step 2: Input the absolute value of an integer
n = abs(int(input()))  # Read user input, convert it to integer, and take the absolute value

# Step 3: Initialize index variable
index = 0  # Setting 'i' to 0

# Step 4: Loop indefinitely
while True:
    # Step 4.1: Calculate the sum of the first 'index' integers
    sum_of_integers = (index * (index + 1)) / 2  # Using the formula for the sum of first 'i' integers
    
    # Step 4.2: Calculate the difference between the sum and 'n'
    difference = sum_of_integers - n  # m = s - n
    
    # Step 4.3: Check if the sum equals 'n'
    if sum_of_integers == n:
        print(index)  # Print the index if sum is equal to 'n'
        break  # Exit the loop
    
    # Step 4.4: Check if the sum is greater than 'n'
    if sum_of_integers > n:
        # Step 4.4.1: Check if the difference is even
        if difference % 2 == 0:  # If m is even
            print(index)  # Print the index if difference is even
            break  # Exit the loop
    
    # Step 4.5: Increment the index variable
    index += 1  # Increase 'i' by 1
