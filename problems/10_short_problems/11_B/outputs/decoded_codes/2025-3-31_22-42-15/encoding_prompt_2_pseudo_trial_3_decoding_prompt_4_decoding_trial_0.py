# Read an integer value and take its absolute value
targetValue = abs(int(input()))

# Initialize the index to 0
index = 0

# Loop until we find the required index
while True:
    # Calculate the sum of the first `index` integers
    currentSum = (index * (index + 1)) // 2
    
    # Calculate the difference between currentSum and targetValue
    difference = currentSum - targetValue
    
    # Check if currentSum equals targetValue
    if currentSum == targetValue:
        print(index)
        break
    
    # If currentSum is greater than targetValue, check the difference
    if currentSum > targetValue:
        if difference % 2 == 0:
            print(index)
            break
    
    # Increment index for the next iteration
    index += 1
