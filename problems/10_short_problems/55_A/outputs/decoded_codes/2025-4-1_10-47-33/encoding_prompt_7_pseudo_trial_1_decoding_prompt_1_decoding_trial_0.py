def checkArrayStatus(size):
    # Initialize an array 'isActive' of boolean values with 'size' elements, all set to True
    isActive = [True] * size
    index = 0
    iteration = 1

    # While iteration is less than or equal to 500000
    while iteration <= 500000:
        # If isActive[index] is True
        if isActive[index]:
            # Set isActive[index] to False
            isActive[index] = False

        # Increase iteration by 1
        iteration += 1
        # Update index to (index + iteration) MOD size
        index = (index + iteration) % size

    # Initialize an array 'activeElements' to store elements of isActive that are still True
    activeElements = []

    # For each element 'element' in isActive
    for element in isActive:
        # If element is True
        if element:
            # Add element to activeElements
            activeElements.append(element)

    # If the length of activeElements is equal to 0
    if len(activeElements) == 0:
        # Print 'YES'
        print('YES')
    else:
        # Print 'NO'
        print('NO')

# Note: When you call this function you'll need to provide the size as an argument.
