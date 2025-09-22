def calculateRemainderAndTotal(n, s):
    quotient, remainder = divmod(n, s)

    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return n

def main():
    n = int(input())
    m = int(input())
    s = int(input())

    adjustedValueN = calculateRemainderAndTotal(n, s)
    adjustedValueM = calculateRemainderAndTotal(m, s)

    print(adjustedValueN * adjustedValueM)

main()
