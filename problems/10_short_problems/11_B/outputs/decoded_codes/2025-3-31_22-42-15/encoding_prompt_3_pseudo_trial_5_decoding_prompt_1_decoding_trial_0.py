# BEGIN

# Read an absolute integer input from the user and store it as 'targetSum'
targetSum = abs(int(input()))

# Initialize the variable 'index' to track the current sequence number
index = 0

# Continuous loop until a break condition is met
while True:
    
    # Calculate the sum of the first 'index' natural numbers
    currentSum = (index * (index + 1)) // 2
    
    # Calculate the difference between currentSum and targetSum
    difference = currentSum - targetSum
    
    # Check if currentSum exactly equals targetSum
    if currentSum == targetSum:
        print(index)  # Output the current index
        break  # Exit the loop

    # Check if currentSum exceeds targetSum
    elif currentSum > targetSum:
        
        # Check if the difference is even
        if difference % 2 == 0:
            print(index)  # Output the current index
            break  # Exit the loop

    # Increment 'index' to check the next number in the next iteration
    index += 1

# END
