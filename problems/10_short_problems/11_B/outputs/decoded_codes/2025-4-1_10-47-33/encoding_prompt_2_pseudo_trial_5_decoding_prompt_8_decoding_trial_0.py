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


def find_smallest_integer():
    try:
        absoluteValue = abs(int(input()))
    except ValueError:
        print("Please enter a valid integer.")
        return

    index = 0

    while True:
        sumOfIntegers = (index * (index + 1)) // 2
        difference = sumOfIntegers - absoluteValue

        if sumOfIntegers == absoluteValue:
            print(index)
            break

        if sumOfIntegers > absoluteValue and difference % 2 == 0:
            print(index)
            break

        index += 1

find_smallest_integer()
