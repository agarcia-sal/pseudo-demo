# Get Input
targetNumber = int(input())

# Initialize Variables
currentInteger = 0

# Loop to Find the Result
while True:
    sumOfIntegers = currentInteger * (currentInteger + 1) // 2
    difference = sumOfIntegers - targetNumber
    
    # Check Conditions
    if sumOfIntegers == targetNumber:
        print(currentInteger)
        break
    elif sumOfIntegers > targetNumber:
        if difference % 2 == 0:
            print(currentInteger)
            break
            
    # Increase currentInteger for the next iteration
    currentInteger += 1
