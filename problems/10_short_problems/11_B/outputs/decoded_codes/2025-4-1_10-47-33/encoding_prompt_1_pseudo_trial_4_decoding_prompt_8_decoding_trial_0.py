inputNumber = abs(int(input()))
index = 0

while True:
    sumOfIntegers = (index * (index + 1)) // 2
    difference = sumOfIntegers - inputNumber
    
    if sumOfIntegers == inputNumber:
        print(index)
        break
    elif sumOfIntegers > inputNumber:
        if difference % 2 == 0:
            print(index)
            break
            
    index += 1
