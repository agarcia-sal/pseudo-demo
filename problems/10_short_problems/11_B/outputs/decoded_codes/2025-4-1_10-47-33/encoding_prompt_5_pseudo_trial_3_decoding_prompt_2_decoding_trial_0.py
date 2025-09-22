# Start of the program

# Step 1: Get the absolute value of the input number
inputNumber = abs(int(input()))

# Step 2: Initialize a counter variable
counter = 0

# Step 3: Start an infinite loop to look for a solution
while True:
    
    # Step 4: Calculate the sum of the first 'counter' integers
    sum_value = (counter * (counter + 1)) // 2  # Using integer division
    
    # Step 5: Calculate the difference between the current sum and the input number
    difference = sum_value - inputNumber
    
    # Step 6: Check if the current sum equals the input number
    if sum_value == inputNumber:
        # Found the solution, print the counter value
        print(counter)
        break  # Exit the loop
    
    # Step 7: Check if the current sum is greater than the input number
    elif sum_value > inputNumber:
        
        # Step 8: Check if the difference is an even number
        if difference % 2 == 0:
            # Found a valid solution, print the counter value
            print(counter)
            break  # Exit the loop
    
    # Step 9: Increment the counter for the next iteration
    counter += 1

# End of the program
