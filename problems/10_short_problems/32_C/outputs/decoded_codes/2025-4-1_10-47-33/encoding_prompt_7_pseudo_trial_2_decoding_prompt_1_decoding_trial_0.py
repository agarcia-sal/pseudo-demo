def calculateRemainderAdjustment(number, divisor):
    quotient = number // divisor
    remainder = number % divisor
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return number

def main():
    n = int(input())
    m = int(input())
    s = int(input())
    adjustedN = calculateRemainderAdjustment(n, s)
    adjustedM = calculateRemainderAdjustment(m, s)
    print(adjustedN * adjustedM)

main()
