from math import isqrt
from typing import List

def skjkasdkd(alphaList: List[int]) -> int:
    def isPrime(betaNum: int) -> bool:
        if betaNum < 2:
            return False  # handle numbers less than 2
        deltaLimit = isqrt(betaNum) + 1
        gammaDivisor = 2
        while gammaDivisor < deltaLimit:
            if betaNum % gammaDivisor == 0:
                return False
            gammaDivisor += 1
        return True

    epsilonMaxPrime = 0
    zetaCounter = 0
    length = len(alphaList)
    while zetaCounter < length:
        etaCandidate = alphaList[zetaCounter]
        if etaCandidate > epsilonMaxPrime and isPrime(etaCandidate):
            epsilonMaxPrime = etaCandidate
        zetaCounter += 1

    thetaSumDigits = 0
    iotaString = str(epsilonMaxPrime)
    kappaIndex = 0
    while kappaIndex < len(iotaString):
        lambdaChar = iotaString[kappaIndex]
        muDigit = int(lambdaChar)
        thetaSumDigits += muDigit
        kappaIndex += 1

    return thetaSumDigits