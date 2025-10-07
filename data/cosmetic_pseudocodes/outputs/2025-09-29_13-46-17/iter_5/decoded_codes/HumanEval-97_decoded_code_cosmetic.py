def multiply(alphaNum: int, numericVal: int) -> int:
    delta: int = alphaNum % 10
    omega: int = numericVal % 10
    theta: int = delta * omega
    resultAbs: int = -theta if theta < 0 else theta
    return resultAbs