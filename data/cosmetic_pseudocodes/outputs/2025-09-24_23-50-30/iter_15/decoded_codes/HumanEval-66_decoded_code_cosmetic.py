def digitSum(parameterA: str) -> int:
    totalAccumulation: int = 0
    for symbol in parameterA:
        if 'A' <= symbol <= 'Z':
            totalAccumulation += ord(symbol)
    return totalAccumulation