def FindIntegerSolution():
    targetValue = abs(int(input()))
    index = 0
    
    while True:
        sum_value = (index * (index + 1)) // 2
        difference = sum_value - targetValue
        
        if sum_value == targetValue:
            print(index)
            break
        elif sum_value > targetValue:
            if difference % 2 == 0:
                print(index)
                break
        
        index += 1
