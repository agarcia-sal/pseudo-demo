# Start
targetSum = abs(int(input()))
index = 0

while True:
    currentSum = (index * (index + 1)) // 2
    difference = currentSum - targetSum
    
    if currentSum == targetSum:
        print(index)
        break
        
    if currentSum > targetSum:
        if difference % 2 == 0:
            print(index)
            break
            
    index += 1
# End
