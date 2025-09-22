# Step 1: Prompt the user to enter a number and take the absolute value of it
number = int(input())
absoluteNumber = abs(number)

# Step 2: Initialize a counter to zero
counter = 0

# Step 3: Enter an indefinite loop to calculate the sum
while True:
    # Step 4: Calculate the sum of the first 'counter' integers
    sum = (counter * (counter + 1)) // 2
    
    # Step 5: Calculate the difference between the sum and 'absoluteNumber'
    difference = sum - absoluteNumber
    
    # Step 6: Check if the sum equals the absolute number
    if sum == absoluteNumber:
        # If they are equal, print the current counter
        print(counter)
        break  # Exit the loop
        
    # Step 7: Check if the sum is greater than the absolute number
    elif sum > absoluteNumber:
        # Check if the difference is an even number
        if difference % 2 == 0:
            # If the difference is even, print the current counter
            print(counter)
            break  # Exit the loop
            
    # Step 8: Increment the counter for the next iteration
    counter += 1
