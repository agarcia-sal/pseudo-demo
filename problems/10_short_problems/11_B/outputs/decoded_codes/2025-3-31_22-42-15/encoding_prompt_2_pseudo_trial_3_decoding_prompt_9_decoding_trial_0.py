# Read an integer value, take its absolute value, and store it
targetValue = abs(int(input()))

# Initialize index to keep track of the sum
index = 0

# Loop to find the smallest index that meets the conditions
while True:
    # Calculate the currentSum using the formula for the sum of the first index integers
    currentSum = (index * (index + 1)) // 2
    
    # Calculate the difference
    difference = currentSum - targetValue
    
    # Check if currentSum is equal to targetValue
    if currentSum == targetValue:
        print(index)
        break
        
    # Check if currentSum is greater than targetValue
    if currentSum > targetValue:
        # Check if the difference is an even number
        if difference % 2 == 0:
            print(index)
            break
            
    # Increment index for the next iteration
    index += 1
