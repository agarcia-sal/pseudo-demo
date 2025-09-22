def checkAllNumbersRemoved(n):
    # Initialize list 'isRemoved' with 'n' elements, all set to True
    isRemoved = [True] * n
    # Initialize index 'currentIndex' to 0
    currentIndex = 0
    # Initialize step 'currentStep' to 1
    currentStep = 1
    
    # While currentStep is less than or equal to 500,000
    while currentStep <= 500000:
        # If isRemoved[currentIndex] is True
        if isRemoved[currentIndex]:
            # Mark isRemoved[currentIndex] as False
            isRemoved[currentIndex] = False
        
        # Increment currentStep by 1
        currentStep += 1
        # Update currentIndex to (currentIndex + currentStep) MOD n
        currentIndex = (currentIndex + currentStep) % n
    
    # Initialize list 'remaining' containing elements from isRemoved that are still True
    remaining = [x for x in isRemoved if x]
    
    # If length of remaining is 0
    if len(remaining) == 0:
        # Print 'YES'
        print('YES')
    else:
        # Print 'NO'
        print('NO')

# Example call to the function (to be provided with n)
# For instance, you would call checkAllNumbersRemoved(n) 
# after getting the input for n depending on your context.
