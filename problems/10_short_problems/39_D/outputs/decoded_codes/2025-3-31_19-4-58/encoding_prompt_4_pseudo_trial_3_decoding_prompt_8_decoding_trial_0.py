def doMain():
    input1 = input()
    input2 = input()
    
    splitInput1 = input1.split()
    splitInput2 = input2.split()
    
    differenceCount = 0
    
    for index in range(3):
        a = int(splitInput1[index])
        b = int(splitInput2[index])

        if a != b:
            differenceCount += 1
    
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Start the program execution
doMain()


     differenceCount = sum(1 for a, b in zip(splitInput1, splitInput2) if int(a) != int(b))
     