# Get Input
inputNumber = abs(int(input()))

# Initialize Variables
i = 0

# Start Infinite Loop
while True:
    # Calculate Sum
    sumOfFirstI = (i * (i + 1)) // 2
    
    # Calculate Difference
    difference = sumOfFirstI - inputNumber
    
    # Check for Exact Match
    if sumOfFirstI == inputNumber:
        print(i)
        break
    
    # Check for Greater Sum
    if sumOfFirstI > inputNumber:
        if difference % 2 == 0:
            print(i)
            break
    
    # Increment Counter
    i += 1
