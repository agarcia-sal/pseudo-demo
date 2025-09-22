targetSum = abs(int(input()))
currentIndex = 0

while True:
    sumOfSeries = currentIndex * (currentIndex + 1) // 2  # Sum of first currentIndex integers
    difference = sumOfSeries - targetSum

    if sumOfSeries == targetSum:
        print(currentIndex)
        break
    
    if sumOfSeries > targetSum and difference % 2 == 0:
        print(currentIndex)
        break
    
    currentIndex += 1
