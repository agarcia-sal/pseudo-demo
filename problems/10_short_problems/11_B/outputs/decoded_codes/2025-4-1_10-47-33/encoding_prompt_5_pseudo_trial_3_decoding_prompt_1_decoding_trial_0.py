# Step 1: Get the absolute value of the input number
inputNumber = abs(int(input()))

# Step 2: Initialize a counter variable
counter = 0

# Step 3: Start an infinite loop to look for a solution
while True:
    
    # Step 4: Calculate the sum of the first 'counter' integers
    sum = (counter * (counter + 1)) // 2
    
    # Step 5: Calculate the difference between the current sum and the input number
    difference = sum - inputNumber
    
    # Step 6: Check if the current sum equals the input number
    if sum == inputNumber:
        # Found the solution, print the counter value
        print(counter)
        break
    
    # Step 7: Check if the current sum is greater than the input number
    elif sum > inputNumber:
        
        # Step 8: Check if the difference is an even number
        if difference % 2 == 0:
            # Found a valid solution, print the counter value
            print(counter)
            break
    
    # Step 9: Increment the counter for the next iteration
    counter += 1
