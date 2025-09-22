def checkArrayStatus(size):
    # Initialize an array 'isActive' with the size 'size' filled with True
    isActive = [True] * size
    index = 0           # Starting index
    iteration = 1       # Starting iteration count

    # Loop for up to 500000 iterations
    while iteration <= 500000:
        # Check if the current index is active
        if isActive[index]:
            isActive[index] = False  # Mark it as inactive

        iteration += 1  # Increment the iteration count
        index = (index + iteration) % size  # Update the index with wrap around

    # Collect all active elements in a new list 'activeElements'
    activeElements = [element for element in isActive if element]

    # Check if there are any active elements left and print the result
    if len(activeElements) == 0:
        print('YES')
    else:
        print('NO')

# Testing practices: Test the function with a variety of inputs
# Example test cases
checkArrayStatus(10)  # Expected output could be 'NO' or 'YES' depending on the logic evaluation
checkArrayStatus(0)   # Edge case: size of 0, expected output 'YES' since there are no elements
checkArrayStatus(1)   # Expected output for a single element array
checkArrayStatus(500) # Average case for reasonable size
