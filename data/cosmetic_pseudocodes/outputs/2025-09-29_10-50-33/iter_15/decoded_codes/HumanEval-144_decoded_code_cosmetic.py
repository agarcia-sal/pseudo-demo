from typing import Union


def simplify(dividendP: str, divisorQ: str) -> bool:
    termsA = dividendP.split("/")
    termsB = divisorQ.split("/")
    factorOne: int = int(termsA[0])
    factorTwo: int = int(termsB[0])
    factorThree: int = int(termsA[1])
    factorFour: int = int(termsB[1])

    accumulatedProductNumerator: int = factorOne * factorTwo
    accumulatedProductDenominator: int = factorThree * factorFour

    fractionCheck: float = accumulatedProductNumerator / accumulatedProductDenominator
    isExactDivision: bool = fractionCheck == int(fractionCheck)

    return isExactDivision