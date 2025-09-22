# Input
targetNumber = abs(int(input()))

# Initialize
index = 0

# Loop
while True:
    # Calculate the sum of the first 'index' natural numbers
    currentSum = index * (index + 1) / 2
    
    # Calculate the difference
    difference = currentSum - targetNumber
    
    # Check Conditions
    if currentSum == targetNumber:
        print(index)
        break
    elif currentSum > targetNumber:
        if difference % 2 == 0:
            print(index)
            break
            
    # Increment the value of index
    index += 1
