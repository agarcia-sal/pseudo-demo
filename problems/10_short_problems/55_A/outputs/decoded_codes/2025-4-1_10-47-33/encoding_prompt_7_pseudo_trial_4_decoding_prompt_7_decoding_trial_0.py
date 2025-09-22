def checkCondition(n):
    # Initialize a list 'isActive' with all values set to True
    isActive = [True] * n
    index = 0  # Start at the first index
    increment = 1  # Start incrementing by 1

    # Loop until increment exceeds 500,000
    while increment <= 500000:
        # If the current index is active, mark it as inactive
        if isActive[index]:
            isActive[index] = False
        
        increment += 1  # Increment the step
        index = (index + increment) % n  # Update index with wrap around using modulus

    # Compile the list of active elements
    activeElements = [element for element in isActive if element]

    # Check if there are any active elements remaining
    if len(activeElements) == 0:
        print('YES')  # All elements are inactive
    else:
        print('NO')  # There are still active elements

# Testing the function with various inputs
checkCondition(10)  # Example test case
checkCondition(1)   # Edge case with 1 element
checkCondition(500) # Larger test case
checkCondition(1000) # Another larger test case
