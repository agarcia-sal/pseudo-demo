# Step 1: Prompt the user to enter an integer value
user_input = int(input())
# Step 2: Take the absolute value and store it in 'targetSum'
targetSum = abs(user_input)
# Step 3: Initialize a counter variable 'index' to zero
index = 0

# Step 4: Enter an indefinite loop
while True:
    # Step 4a: Calculate the sum of the first 'index' natural numbers
    currentSum = (index * (index + 1)) // 2  # Sum of first 'index' natural numbers
    # Step 4b: Calculate the difference between 'currentSum' and 'targetSum'
    difference = currentSum - targetSum
    
    # Step 4c: Check if 'currentSum' is equal to 'targetSum'
    if currentSum == targetSum:
        print(index)  # Output the value of 'index'
        break  # Exit the loop
        
    # Step 4d: Check if 'currentSum' is greater than 'targetSum'
    if currentSum > targetSum:
        # Check if 'difference' is an even number
        if difference % 2 == 0:
            print(index)  # Output the value of 'index'
            break  # Exit the loop
            
    # Step 4e: Increment the 'index' variable by one
    index += 1
