def findIntegerWithTriangleNumber():
    inputValue = int(input())
    absoluteValue = abs(inputValue)
    counter = 0
    
    while True:
        triangularNumber = (counter * (counter + 1)) // 2
        difference = triangularNumber - absoluteValue
        
        if triangularNumber == absoluteValue:
            print(counter)
            break
        elif triangularNumber > absoluteValue:
            if difference % 2 == 0:
                print(counter)
                break
        counter += 1


def findIntegerWithTriangleNumber(inputValue):
    absoluteValue = abs(inputValue)
    counter = 0
    
    while True:
        triangularNumber = (counter * (counter + 1)) // 2
        difference = triangularNumber - absoluteValue
        
        if triangularNumber == absoluteValue:
            return counter
        elif triangularNumber > absoluteValue:
            if difference % 2 == 0:
                return counter
        counter += 1
