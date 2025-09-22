def checkAllNumbersRemoved(n):
    # Initialize the list `isRemoved` with `n` elements, all set to True
    isRemoved = [True] * n
    # Initialize index `currentIndex` to 0
    currentIndex = 0
    # Initialize step `currentStep` to 1
    currentStep = 1
    
    # While `currentStep` is less than or equal to 500000
    while currentStep <= 500000:
        # If `isRemoved[currentIndex]` is True
        if isRemoved[currentIndex] is True:
            # Mark `isRemoved[currentIndex]` as False
            isRemoved[currentIndex] = False
        
        # Increment `currentStep` by 1
        currentStep += 1
        # Update `currentIndex` to `(currentIndex + currentStep) % n`
        currentIndex = (currentIndex + currentStep) % n
    
    # Initialize list `remaining` containing elements from `isRemoved` that are still True
    remaining = [value for value in isRemoved if value is True]
    
    # If length of `remaining` is 0
    if len(remaining) == 0:
        print('YES')
    else:
        print('NO')
