def calculateRemainderAndProduct():
    def mc(number, divisor):
        quotient = number // divisor
        remainder = number % divisor
        if remainder > 0:
            return remainder * (quotient + 1)
        else:
            return number

    n = int(input())
    m = int(input())
    s = int(input())
    
    resultA = mc(n, s)
    resultB = mc(m, s)
    
    print(resultA * resultB)

calculateRemainderAndProduct()
