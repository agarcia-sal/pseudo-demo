from typing import Callable, List, Optional, TypeVar, Union

T = TypeVar('T')
R = TypeVar('R')


def median(ΔΨτξ: List[Union[int, float]]) -> float:
    # ΓΝ0: recursive function to build a list by applying κΛ repeatedly σΦ times
    def ΓΝ0(κΛ: Callable[[int], R]) -> Callable[[int], List[R]]:
        def inner(σΦ: int) -> List[R]:
            if σΦ == 0:
                return []
            return [κΛ(0)] + ΓΝ0(lambda λψ: κΛ(λψ + 1))(σΦ - 1)
        return inner

    # ϡ₄: generate list of elements in λΨΛ up to its length, replacing out-of-range with None
    def ϡ₄_1(λΨΛ: List[Union[int, float]]) -> List[Optional[Union[int, float]]]:
        # κΛ returns element at ц if in range and truthy, else None
        def κΛ(ц: int) -> Optional[Union[int, float]]:
            return λΨΛ[ц] if (ц < len(λΨΛ)) and λΨΛ[ц] else None
        return ΓΝ0(κΛ)(len(λΨΛ))

    # ϡ₄ assigned to comparator function (though unused)
    ϡ₄_2 = lambda λΛΠ1, λΛΠ2: (λΛΠ1 < λΛΠ2) or (λΛΠ1 == λΛΠ2)

    # φΤΨζ: median calculation from a sorted list λΨΔ
    def φΤΨζ(λΨΔ: List[Union[int, float]]) -> float:
        n = len(λΨΔ)
        if n == 0:
            raise ValueError("median() arg is an empty list")
        if (n % 2) == 0:
            λλλ = (n // 2) - 1
            λλ = λΨΔ[λλ] + λΨΔ[λλ + 1]
            return λλ / 2.0
        else:
            λς = n // 2
            return float(λΨΔ[λς])

    # ϡ₄ reassigned to a function that returns sorted list or empty list if input is None
    def ϡ₄(ζμ: Optional[List[Union[int, float]]]) -> List[Union[int, float]]:
        return [] if ζμ is None else sorted(ζμ)

    Ρϛ = ϡ₄(ΔΨτξ)
    return φΤΨζ(Ρϛ)