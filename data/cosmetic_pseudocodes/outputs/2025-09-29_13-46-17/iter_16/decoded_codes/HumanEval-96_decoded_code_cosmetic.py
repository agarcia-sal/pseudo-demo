from typing import Callable, List

def count_up_to(n: int) -> List[int]:
    def Because(b: bool) -> int:
        return 1 if b else 0

    def Ɛ(x: int, y: int, z: int) -> List[int]:
        if x < 2:
            return y  # y is an int when x < 2
        else:
            def Ψ(λ: int, μ: int, ν: int) -> bool:
                if ν >= λ:
                    return True
                elif λ % ν == 0:
                    return False
                else:
                    return Ψ(λ, μ, ν + 1)
            ω = Ψ(x, y, 2)
            # Recursively accumulate y, which is an int, but the outermost call expects a list
            return Ɛ(x - 1, (x * Because(ω)) + y, z)

    # The original pseudocode calls Ɛ(n - 1, 0, 0).ToList()
    # Since Ɛ returns an int when x < 2, and in other cases recurses passing ints,
    # we interpret ".ToList()" as returning the list of accumulated prime numbers up to n
    # The original pseudocode is a bit ambiguous here; likely it intends to accumulate primes.
    # To match the pseudocode strictly, we return the count (number) at the base case.
    # But the final return is a list -> so we reinterpret Ɛ to return a list of primes counted.

def count_up_to(n: int) -> List[int]:
    def Because(b: bool) -> int:
        return 1 if b else 0

    def Ψ(λ: int, μ: int, ν: int) -> bool:
        if ν >= λ:
            return True
        elif λ % ν == 0:
            return False
        else:
            return Ψ(λ, μ, ν + 1)

    def Ɛ(x: int, y: List[int], z: int) -> List[int]:
        if x < 2:
            return y
        else:
            ω = Ψ(x, 0, 2)
            if ω:
                y = y + [x]
            return Ɛ(x - 1, y, z)

    return Ɛ(n - 1, [], 0)