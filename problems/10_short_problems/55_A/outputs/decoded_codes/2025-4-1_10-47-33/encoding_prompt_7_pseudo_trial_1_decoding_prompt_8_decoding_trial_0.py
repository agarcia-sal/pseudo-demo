def checkArrayStatus(size):
    isActive = [True] * size
    index = 0
    iteration = 1

    while iteration <= 500000:
        if isActive[index]:
            isActive[index] = False
        
        iteration += 1
        index = (index + iteration) % size

    activeElements = [element for element in isActive if element]

    if len(activeElements) == 0:
        print('YES')
    else:
        print('NO')

# Example of how to call the function with user input
size = int(input())
checkArrayStatus(size)
