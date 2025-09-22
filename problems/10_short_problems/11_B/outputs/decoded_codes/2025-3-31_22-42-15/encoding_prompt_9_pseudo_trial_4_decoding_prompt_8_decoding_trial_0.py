# Begin
absoluteValue = abs(int(input()))
currentIndex = 0

while True:
    sumOfNumbers = (currentIndex * (currentIndex + 1)) // 2
    difference = sumOfNumbers - absoluteValue
    
    if sumOfNumbers == absoluteValue:
        print(currentIndex)
        break
    elif sumOfNumbers > absoluteValue:
        if difference % 2 == 0:
            print(currentIndex)
            break
    
    currentIndex += 1
# End
