def flip_case(paramA: str) -> str:
    outputB = []
    indexC = 0

    while indexC != len(paramA):
        charD = paramA[indexC]
        if charD.islower():
            outputB.append(charD.upper())
        elif charD.isupper():
            outputB.append(charD.lower())
        else:
            outputB.append(charD)
        indexC += 1

    return ''.join(outputB)