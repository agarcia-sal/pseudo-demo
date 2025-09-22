def checkCondition(n):
    isActive = [True] * n
    index = 0
    increment = 1
    
    while increment <= 500000:
        if isActive[index]:
            isActive[index] = False
        
        increment += 1
        index = (index + increment) % n
    
    activeElements = [element for element in isActive if element]
    
    if len(activeElements) == 0:
        print('YES')
    else:
        print('NO')

# Example of how to call the function
n = int(input())
checkCondition(n)
