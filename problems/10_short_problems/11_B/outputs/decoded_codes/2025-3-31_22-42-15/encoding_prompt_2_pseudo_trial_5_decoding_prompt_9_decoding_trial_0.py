# Read an integer from the user and store its absolute value in targetSum
targetSum = abs(int(input()))

# Initialize currentIndex to keep track of the current index
currentIndex = 0

# Infinite loop until a valid condition is met
while True:
    # Calculate the sum of the first currentIndex integers
    sumOfSeries = (currentIndex * (currentIndex + 1)) // 2
    
    # Calculate the difference between the sumOfSeries and targetSum
    difference = sumOfSeries - targetSum

    # Check if sumOfSeries is equal to targetSum
    if sumOfSeries == targetSum:
        print(currentIndex)
        break
        
    # If sumOfSeries is greater than targetSum, check difference
    if sumOfSeries > targetSum:
        if difference % 2 == 0:
            print(currentIndex)
            break
            
    # Increment currentIndex for the next iteration
    currentIndex += 1
