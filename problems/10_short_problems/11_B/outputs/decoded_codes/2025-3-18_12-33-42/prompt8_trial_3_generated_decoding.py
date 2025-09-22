# Get input from the user and convert to an absolute value
inputValue = abs(int(input()))

# Initialize the counter
currentInteger = 0

# Infinite loop to find the result
while True:
    # Calculate the sum of integers from 0 to currentInteger
    sum = (currentInteger * (currentInteger + 1)) // 2
    # Calculate the difference between the sum and the absolute input value
    difference = sum - inputValue
    
    # Check conditions
    if sum == inputValue:
        print(currentInteger)
        break
    if sum > inputValue:
        if difference % 2 == 0:
            print(currentInteger)
            break
    
    # Increment currentInteger to check the next integer
    currentInteger += 1
