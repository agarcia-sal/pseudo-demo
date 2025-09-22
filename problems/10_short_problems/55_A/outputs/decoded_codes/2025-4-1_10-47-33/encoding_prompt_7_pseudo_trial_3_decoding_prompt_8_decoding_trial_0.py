def checkAllNumbersRemoved(n):
    isRemoved = [True] * n
    currentIndex = 0
    currentStep = 1
    
    while currentStep <= 500000:
        if isRemoved[currentIndex]:
            isRemoved[currentIndex] = False
        
        currentStep += 1
        currentIndex = (currentIndex + currentStep) % n
    
    remaining = [x for x in isRemoved if x]
    
    if len(remaining) == 0:
        print('YES')
    else:
        print('NO')
