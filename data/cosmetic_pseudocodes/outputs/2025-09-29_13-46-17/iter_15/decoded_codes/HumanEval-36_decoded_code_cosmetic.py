from typing import List

def fizz_buzz(integer_n: int) -> int:
    # Collect integers from 0 to integer_n - 1 divisible by 11 or 13
    div_set = {i for i in range(integer_n) if i % 11 == 0 or i % 13 == 0}

    # Concatenate their string representations in ascending order
    concat_str = "".join(str(x) for x in sorted(div_set))

    # Count the number of '7's in the concatenated string
    count_sevens: int = 0
    for ch in concat_str:
        count_sevens += 1 if ch == '7' else 0

    return count_sevens