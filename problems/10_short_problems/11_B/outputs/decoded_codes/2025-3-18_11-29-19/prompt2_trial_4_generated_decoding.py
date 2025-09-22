# Start

# Receive Input
targetValue = abs(int(input()))

# Initialize a Counter
index = 0

# Infinite Loop
while True:
    # Calculate the sum of the first "index" natural numbers
    currentSum = (index * (index + 1)) // 2
    
    # Calculate the difference between currentSum and targetValue
    difference = currentSum - targetValue
    
    # Check if sum equals targetValue
    if currentSum == targetValue:
        print(index)
        break  # Terminate the loop
        
    # Check if sum exceeds targetValue
    if currentSum > targetValue:
        if difference % 2 == 0:  # Check if difference is an even number
            print(index)
            break  # Terminate the loop
            
    # Increment the counter
    index += 1

# End
