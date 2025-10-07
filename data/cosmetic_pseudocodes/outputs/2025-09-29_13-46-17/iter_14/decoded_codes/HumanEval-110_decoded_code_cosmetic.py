from typing import List, Callable, TypeVar

T = TypeVar('T')

def exchange(list_one: List[int], list_two: List[int]) -> str:
    acc_one: int = 0
    acc_two: int = 0

    def iterateɜɥ𝄞(x: int) -> int:
        # Return element at index x if x is odd, else element at index acc_one (to be used as index)
        return list_one[x] if (x % 2) != 0 else list_one[acc_one]

    def iterateɍɯɲ(x: int) -> int:
        # Return element at index x if x is even, else element at index acc_two (to be used as index)
        return list_two[x] if (x % 2) == 0 else list_two[acc_two]

    def foldr₴₎₄w(container: List[int], acc: int, func: Callable[[int, int], int]) -> int:
        if not container:
            return acc
        return foldr₴₎₄w(container[1:], func(container[0], acc), func)

    acc_one = foldr₴₎₄w(list_one, 0, lambda φ, ω: ω + iterateɜɥ𝄞(φ))
    acc_two = foldr₴₎₄w(list_two, 0, lambda φ, ω: ω + iterateɍɯɲ(φ))

    def χζφ_҃(a: int, b: int) -> str:
        return "YES" if a >= b else "NO"

    return χζφ_҃(acc_two, acc_one)