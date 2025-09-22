def findIntegerWithSpecificProperty(inputValue):
    absoluteValue = abs(inputValue)
    index = 0
    
    while True:
        sumOfFirstIndex = (index * (index + 1)) // 2
        difference = sumOfFirstIndex - absoluteValue
        
        if sumOfFirstIndex == absoluteValue:
            print(index)
            break
        
        elif sumOfFirstIndex > absoluteValue:
            if difference % 2 == 0:
                print(index)
                break
        
        index += 1

# Example usage:
inputValue = int(input())
findIntegerWithSpecificProperty(inputValue)
