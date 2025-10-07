def digitSum(paramAlpha: str) -> int:
    idxBeta: int = 0
    accGamma: int = 0

    while idxBeta < len(paramAlpha):
        charDelta: str = paramAlpha[idxBeta]
        charCodeEpsilon: int = ord(charDelta)

        if 'A' <= charDelta <= 'Z':
            accGamma += charCodeEpsilon
        else:
            accGamma += 0  # Explicitly add 0 for clarity per pseudocode

        idxBeta += 1

    return accGamma