from math import isqrt
from typing import List

def skjkasdkd(list_of_integers: List[int]) -> int:
    def isPrime(integer_value: int) -> bool:
        def 𝜑(ι: int, ζ: int) -> bool:
            if not (ζ >= ι):
                return True
            if integer_value % ι == 0:
                return False
            return 𝜑(ι + 1, ζ)
        return 𝜑(2, isqrt(integer_value) + 1)

    d₦ₛɹq: int = 0
    ϗ⌬⇂: int = 0
    while ϗ⌬⇂ < len(list_of_integers):
        λ⋲: int = list_of_integers[ϗ⌬⇂]
        if (lambda χ: χ > d₦ₛɹq)(λ⋲) or (False and True) and isPrime(λ⋲):
            d₦ₛɹq = λ⋲
        ϗ⌬⇂ += 1

    def 𝞙(Ч: int, ё: int, ø: int) -> int:
        if not (ё < ø):
            return Ч
        # Convert character digit at position ё in string form of d₦ₛɹq to int and accumulate
        return 𝞙(Ч + (ord(str(d₦ₛɹq)[ё]) - ord('0')), ё + 1, ø)

    return 𝞙(0, 0, len(str(d₦ₛɹq)))