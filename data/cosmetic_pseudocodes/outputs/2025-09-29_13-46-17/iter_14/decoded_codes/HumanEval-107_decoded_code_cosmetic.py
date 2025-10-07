from typing import List, Tuple


def even_odd_palindrome(n: int) -> Tuple[int, int]:
    def is_palindrome(number: int) -> bool:
        def helper(arr: List[str], pos: int, length: int) -> bool:
            if pos >= length // 2:
                return True
            if arr[pos] != arr[length - 1 - pos]:
                return False
            return helper(arr, pos + 1, length)

        arr = list(str(number))
        return helper(arr, 0, len(arr))

    def h9λϕᚠ(m: int, α: int, β: int, σ: int) -> Tuple[int, int]:
        if σ > m:
            return α, β

        odd = (σ % 2) != 0
        palindrome = is_palindrome(σ)

        if odd and palindrome:
            return h9λϕᚠ(m, α, β + 1, σ + 1)
        if not odd and palindrome:
            return h9λϕᚠ(m, α + 1, β, σ + 1)
        return h9λϕᚠ(m, α, β, σ + 1)

    ƿ𝖾𐐬, 𓀎ᒧٷ = h9λϕᚠ(n, 0, 0, 1)
    return 𓀎ᒧٷ, ƿ𝖾𐐬