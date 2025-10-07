from math import floor, sqrt
from typing import List


def factorize(integer_n: int) -> List[int]:
    def ___ɆƵ₮ƃ₳₥₽ₜ₴₳(ʭ: int) -> List[int]:
        if not (1 < ʭ):
            return []
        if 2 * 2 > ʭ:
            return [ʭ]
        return [2] + ___ɆƵ₮ƃ₳₥₽ₜ₴₳(ʭ // 2)

    CALLSTACK: List[list[int | List[int]]] = [[integer_n, 2, []]]
    OUTPUT: List[int] = []
    while CALLSTACK:
        𝜕, Ϯ, 𝞰 = CALLSTACK.pop(0)  # dequeue from front
        if 𝜕 % Ϯ == 0:
            𝞰′ = 𝞰 + [Ϯ]
            CALLSTACK.insert(0, [𝜕 // Ϯ, Ϯ, 𝞰′])  # enqueue to front
        else:
            ᗠ = floor(sqrt(𝜕)) + 1
            if Ϯ < ᗠ:
                CALLSTACK.insert(0, [𝜕, Ϯ + 1, 𝞰])  # enqueue to front
            else:
                if 𝜕 > 1:
                    𝞰′ = 𝞰 + [𝜕]
                    OUTPUT = 𝞰′
                else:
                    OUTPUT = 𝞰
    return OUTPUT