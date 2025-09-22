# Begin of the program

# Step 1: Get the absolute value of input and convert it to an integer
targetValue = abs(int(input()))  # Taking input from the user

# Step 2: Initialize counter variable
index = 0  # Start with an index of 0

# Step 3: Start an infinite loop to find the value
while True:
    
    # Calculate the sum of first 'index' natural numbers
    sum_of_natural_numbers = (index * (index + 1)) // 2  # Using integer division

    # Calculate the difference between the sum and the targetValue
    difference = sum_of_natural_numbers - targetValue
    
    # Step 4: Check if the sum matches the targetValue
    if sum_of_natural_numbers == targetValue:
        print(index)  # Output the current index and exit the loop
        break  # Exit the infinite loop

    # Step 5: Check if the sum exceeds the targetValue
    elif sum_of_natural_numbers > targetValue:
        
        # Step 6: Check if the difference is even
        if difference % 2 == 0:  # Checking if the difference is even
            print(index)  # Output the current index and exit the loop
            break  # Exit the infinite loop
    
    # Increment the index for the next iteration
    index += 1  # Increase index by 1 for the next loop

# End of the program
