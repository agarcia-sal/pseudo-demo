def main():
    firstInput = input()
    secondInput = input()

    firstSet = firstInput.split()
    secondSet = secondInput.split()

    differenceCount = 0 

    for index in range(3):
        firstNumber = int(firstSet[index])
        secondNumber = int(secondSet[index])

        if firstNumber != secondNumber:
            differenceCount += 1

    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Start the program
main()
