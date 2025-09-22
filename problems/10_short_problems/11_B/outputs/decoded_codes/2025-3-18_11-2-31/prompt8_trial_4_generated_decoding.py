# Get Input
inputValue = int(input())
targetSum = abs(inputValue)

# Initialize Counter
counter = 0

# Loop Until Finding Result
while True:
    # Calculate Sum
    currentSum = counter * (counter + 1) // 2
    
    # Calculate Difference
    difference = currentSum - targetSum
    
    # Check Conditions
    if currentSum == targetSum:
        print(counter)
        break
    elif currentSum > targetSum:
        if difference % 2 == 0:
            print(counter)
            break
    
    # Increment Counter
    counter += 1
