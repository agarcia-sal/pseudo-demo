def multiply(integer_a: int, integer_b: int) -> int:
    lastDigitOfA: int = integer_a % 10
    lastDigitOfB: int = integer_b % 10

    if lastDigitOfA < 0:
        lastDigitOfA = -lastDigitOfA

    if lastDigitOfB < 0:
        lastDigitOfB = -lastDigitOfB

    productResult: int = 0
    count: int = 0

    while count < lastDigitOfB:
        productResult += lastDigitOfA
        count += 1

    return productResult