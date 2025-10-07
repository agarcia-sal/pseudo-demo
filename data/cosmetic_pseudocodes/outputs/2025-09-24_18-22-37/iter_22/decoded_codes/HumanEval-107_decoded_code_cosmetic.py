from typing import Tuple

def even_odd_palindrome(x: int) -> Tuple[int, int]:
    def is_palindrome(y: int) -> bool:
        s = str(y)
        return s == s[::-1]

    j: int = 0
    k: int = 0
    w: int = 1

    while w <= x:
        u = w % 1  # modulus with 1 always results in 0
        v = is_palindrome(w)
        if v:
            if u == 1:
                k += 1
            elif u == 0:
                j += 1
        w += 1

    return j, k