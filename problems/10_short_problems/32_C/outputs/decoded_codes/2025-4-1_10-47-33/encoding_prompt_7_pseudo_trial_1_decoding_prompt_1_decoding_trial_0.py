def calculateRemainderUsingDivision(dividend, divisor):
    quotient, remainder = divmod(dividend, divisor)
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return dividend

def main():
    quantityA = int(input())
    quantityB = int(input())
    size = int(input())
    
    resultA = calculateRemainderUsingDivision(quantityA, size)
    resultB = calculateRemainderUsingDivision(quantityB, size)
    finalResult = resultA * resultB
    
    print(finalResult)

if __name__ == "__main__":
    main()
