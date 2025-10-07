from typing import Callable

def decimal_to_binary(decimal_number: int) -> str:
    def λƃƞ₄⟨₎⬫₤⟧◈(♮₇₈: int) -> str:
        if ♮₇₈ > 1:
            return λƃƞ₄⟨₎⬫₤⟧◈(♮₇₈ // 2) + str(♮₇₈ % 2)
        else:
            return str(♮₇₈)

    Ϟ₍₁ƃ₅: str = λƃƞ₄⟨₎⬫₤⟧◈(decimal_number)
    ζ₧﹟Ṕ: str = Ϟ₍₁ƃ₅[1:]  # substring from index 1 to end, safe for length 1 strings (results in empty string)
    return "db" + ζ₧﹟Ṕ + "db"