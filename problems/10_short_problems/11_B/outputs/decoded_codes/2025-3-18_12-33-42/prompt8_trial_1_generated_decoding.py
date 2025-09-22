# Get Input
inputNumber = input()
targetValue = abs(int(inputNumber))

# Initialize Starting Point
index = 0

# Begin Infinite Loop
while True:
    # Calculate Sum
    sumOfNumbers = (index * (index + 1)) // 2  # Using integer division

    # Calculate Difference
    difference = sumOfNumbers - targetValue

    # Check Conditions
    if sumOfNumbers == targetValue:
        print(index)
        break
    elif sumOfNumbers > targetValue:
        if difference % 2 == 0:
            print(index)
            break

    # Increment Index
    index += 1
