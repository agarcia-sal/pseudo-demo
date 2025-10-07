from typing import Callable

def modp(integer_n: int, integer_p: int) -> int:
    def powerCalc(currentCount: int) -> int:
        if currentCount == integer_n:
            return 1
        auxResult = powerCalc(currentCount + 1)
        return (auxResult + auxResult) % integer_p
    return powerCalc(0)