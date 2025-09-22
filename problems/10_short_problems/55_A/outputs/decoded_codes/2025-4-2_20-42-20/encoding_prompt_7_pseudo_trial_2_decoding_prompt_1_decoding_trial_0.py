def checkNumbersUpTo(n):
    # Initialize a list to keep track of numbers
    booleanList = [True] * n
    
    # Initialize indices for tracking
    currentIndex = 0
    iterationCounter = 1
    
    # Start iterating up to a maximum of 500000
    while iterationCounter <= 500000:
        # If the current index is marked as TRUE, mark it as FALSE
        if booleanList[currentIndex] is True:
            booleanList[currentIndex] = False
        
        # Move to the next index
        iterationCounter += 1
        currentIndex = (currentIndex + iterationCounter) % n
    
    # Filter the list to find all still TRUE values
    remainingTrueValues = [value for value in booleanList if value]
    
    # Check if there are any TRUE values left
    if len(remainingTrueValues) == 0:
        print('YES')
    else:
        print('NO')

# Read an integer input for n
n = int(input())
checkNumbersUpTo(n)
