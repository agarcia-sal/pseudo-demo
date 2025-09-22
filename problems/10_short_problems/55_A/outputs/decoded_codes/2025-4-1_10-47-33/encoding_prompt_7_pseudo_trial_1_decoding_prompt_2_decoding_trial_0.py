def checkArrayStatus(size):
    # Initialize an array 'isActive' with 'size' elements, all set to True
    isActive = [True] * size
    index = 0
    iteration = 1

    # Loop for up to 500000 iterations
    while iteration <= 500000:
        if isActive[index] is True:
            isActive[index] = False
        
        iteration += 1
        index = (index + iteration) % size

    # Initialize 'activeElements' to store elements of isActive that are still True
    activeElements = []

    # Collect all active elements
    for element in isActive:
        if element is True:
            activeElements.append(element)

    # Check if 'activeElements' is empty
    if len(activeElements) == 0:
        print('YES')
    else:
        print('NO')

# Example of how to call the function
# Uncomment the line below to test the function with an example size
# checkArrayStatus(int(input()))  # Replace this line as per your testing needs
