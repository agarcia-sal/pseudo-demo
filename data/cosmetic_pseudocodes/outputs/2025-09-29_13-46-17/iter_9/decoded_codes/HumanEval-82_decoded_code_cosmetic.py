from typing import Union

def prime_length(ξψωκθ: Union[str, bytes, list, tuple]) -> bool:
    def ς(n: int) -> bool:
        if n == 0 or n == 1:
            return False

        def ϟ(λχ: int, β: int) -> bool:
            if β > λχ - 1:
                return True
            if λχ % β == 0:
                return False
            return ϟ(λχ, β + 1)

        return ϟ(n, 2)

    μ₉: bool = ς(len(ξψωκθ))
    return μ₉