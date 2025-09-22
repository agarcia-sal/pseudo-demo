# Input Handling
absoluteInput = abs(int(input()))

# Initialize a Counter
index = 0

# Infinite Loop for Calculation
while True:
    # Calculate the sum of the first 'index' integers
    currentSum = (index * (index + 1)) / 2
    
    # Calculate the difference between currentSum and absoluteInput
    difference = currentSum - absoluteInput
    
    # Check Conditions
    if currentSum == absoluteInput:
        # Output the value of index as the result
        print(index)
        break
    elif currentSum > absoluteInput:
        if difference % 2 == 0:
            # Output the value of index as the result
            print(index)
            break
    
    # Increment the Counter
    index += 1
