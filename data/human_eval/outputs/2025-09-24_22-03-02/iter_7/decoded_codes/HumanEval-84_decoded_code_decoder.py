def solve(N: int) -> str:
    digitSum = 0
    for character in str(N):
        digitSum += int(character)
    binaryResult = bin(digitSum)[2:]
    return binaryResult