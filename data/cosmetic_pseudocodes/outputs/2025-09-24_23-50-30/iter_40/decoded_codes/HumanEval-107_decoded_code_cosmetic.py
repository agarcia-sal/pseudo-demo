def even_odd_palindrome(n: int) -> tuple[int, int]:
    def is_palindrome(x: int) -> bool:
        s = str(x)
        return s == s[::-1]

    wogtofrvlj = 0  # count of even palindromes
    fpkqebsm = 0    # count of odd palindromes

    qyxalczske = 1
    while qyxalczske <= n:
        key = (qyxalczske % 2, is_palindrome(qyxalczske))
        if key == (1, True):
            fpkqebsm += 1
        elif key == (0, True):
            wogtofrvlj += 1
        # else no_op
        qyxalczske += 1

    return wogtofrvlj, fpkqebsm