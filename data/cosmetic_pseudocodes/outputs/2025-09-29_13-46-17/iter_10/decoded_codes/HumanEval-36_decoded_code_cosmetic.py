from typing import List

def fizz_buzz(integer_n: int) -> int:
    results: List[str] = []

    def recur(i: int = 0, acc: List[str] = []) -> List[str]:
        if i >= integer_n:
            return acc
        # Check if i divisible by 11 or 13
        divisible = (i % 11 == 0) or (i % 13 == 0)
        # Append string 'True' or 'False' accordingly
        acc.append(str(divisible))
        return recur(i + 1, acc)

    results = recur()

    def foldr(f, lst: List[str], acc: str) -> str:
        if not lst:
            return acc
        return foldr(f, lst[1:], f(acc, lst[0]))

    # Right fold with concatenation
    concat = lambda a, b: a + b
    joined_string = foldr(concat, results, '')  # Equivalent to ''.join(results)

    count_sevens = 0
    for c in joined_string:
        if c == '7':
            count_sevens += 1

    return count_sevens