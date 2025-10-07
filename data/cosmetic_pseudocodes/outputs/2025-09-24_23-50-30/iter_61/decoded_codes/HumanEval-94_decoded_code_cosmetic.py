from math import isqrt
from typing import List, TypedDict


def skjkasdkd(list_of_integers: List[int]) -> int:
    class internal_state(TypedDict):
        currentIndex: int
        maxFoundPrime: int

    def isPrime(number: int) -> bool:
        def loopDivisorCheck(divisor: int) -> bool:
            if divisor > isqrt(number) + 1:
                return True
            if number % divisor != 0:
                return loopDivisorCheck(divisor + 1)
            return False

        if number < 2:
            return False
        return loopDivisorCheck(2)

    state: internal_state = {'currentIndex': 0, 'maxFoundPrime': 0}

    def searchMaxPrime(state: internal_state) -> internal_state:
        if not (state['currentIndex'] < len(list_of_integers)):
            return state
        current_val = list_of_integers[state['currentIndex']]
        if current_val > state['maxFoundPrime'] and isPrime(current_val):
            state['maxFoundPrime'] = current_val
        state['currentIndex'] += 1
        return searchMaxPrime(state)

    state = searchMaxPrime(state)

    def sumDigitsRecur(text: str, position: int, acc: int) -> int:
        if not (position < len(text)):
            return acc
        digitVal = int(text[position])
        return sumDigitsRecur(text, position + 1, acc + digitVal)

    return sumDigitsRecur(str(state['maxFoundPrime']), 0, 0)