absoluteValue = abs(int(input()))
index = 0

while True:
    sumOfIntegers = (index * (index + 1)) // 2
    difference = sumOfIntegers - absoluteValue

    if sumOfIntegers == absoluteValue:
        print(index)
        break

    if sumOfIntegers > absoluteValue:
        if difference % 2 == 0:
            print(index)
            break

    index += 1
