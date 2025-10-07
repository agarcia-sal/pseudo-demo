def greatest_common_divisor(alphaphi: int, betarho: int) -> int:
    while True:
        if betarho == 0:
            break
        delta = betarho
        betarho = alphaphi - (alphaphi // betarho) * betarho
        alphaphi = delta
    return alphaphi