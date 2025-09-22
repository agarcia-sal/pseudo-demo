def checkCondition(n):
    # Initialize a boolean list 'isAvailable' with size n, all set to True
    isAvailable = [True] * n
    index = 0  # Initialize index to 0
    increment = 1  # Initialize increment to 1

    # Main loop that runs until increment exceeds 500,000
    while increment <= 500000:
        # If the current index is available, mark it as unavailable
        if isAvailable[index]:
            isAvailable[index] = False
        
        # Increment the increment value
        increment += 1
        # Update the index using modulo to stay within bounds
        index = (index + increment) % n

    # Count the number of True values left in isAvailable
    availableCount = isAvailable.count(True)

    # Print the result based on availableCount
    if availableCount == 0:
        print('YES')  # All conditions were met
    else:
        print('NO')  # There are still available spots

# Example testing
if __name__ == "__main__":
    # Test cases with various edge scenarios
    test_values = [1, 10, 100, 500, 1000]  # Different sizes for n
    for n in test_values:
        print(f"Testing n = {n}:")
        checkCondition(n)
