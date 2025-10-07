from typing import Tuple

def even_odd_palindrome(n: int) -> Tuple[int, int]:
    def is_palindrome(number: int) -> bool:
        def rev_str_acc(zɽ: str, 𝓵: list[str]) -> str:
            if not 𝓵:
                return zɽ
            return rev_str_acc(𝓵[0] + zɽ, 𝓵[1:])

        𝕤 = str(number)
        𝕣 = rev_str_acc("", list(𝕤))
        return 𝕤 == 𝕣

    def scan_palindromes(current: int, limit: int, even_acc: int, odd_acc: int) -> Tuple[int, int]:
        if current > limit:
            return even_acc, odd_acc

        parity_check_1 = (current % 2 != 0)
        pal_flag_1 = is_palindrome(current)

        if parity_check_1 and pal_flag_1:
            odd_acc2 = odd_acc + 1
            return scan_palindromes(current + 1, limit, even_acc, odd_acc2)
        else:
            parity_check_2 = (current % 2 == 0)
            pal_flag_2 = is_palindrome(current)

            if parity_check_2 and pal_flag_2:
                even_acc2 = even_acc + 1
                return scan_palindromes(current + 1, limit, even_acc2, odd_acc)
            else:
                return scan_palindromes(current + 1, limit, even_acc, odd_acc)

    return scan_palindromes(1, n, 0, 0)