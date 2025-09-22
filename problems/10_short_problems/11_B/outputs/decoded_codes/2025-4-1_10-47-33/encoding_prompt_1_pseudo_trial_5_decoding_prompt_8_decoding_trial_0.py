# Input
input_value = int(input())
targetNumber = abs(input_value)

# Initialize
index = 0

# Loop
while True:
    currentSum = index * (index + 1) // 2
    difference = currentSum - targetNumber
    
    # Check Conditions
    if currentSum == targetNumber:
        print(index)
        break
    elif currentSum > targetNumber:
        if difference % 2 == 0:
            print(index)
            break
    
    # Increment
    index += 1
