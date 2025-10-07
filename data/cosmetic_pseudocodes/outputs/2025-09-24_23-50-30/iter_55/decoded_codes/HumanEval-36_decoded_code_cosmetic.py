from typing import List


def fizz_buzz(random_x: int) -> int:
    fresh_agg: List[int] = []

    def helper_iterate(counter_y: int) -> None:
        if counter_y < random_x:
            # Condition: NOT (counter_y % 11 != 0 AND counter_y % 13 != 0)
            # Means counter_y divisible by 11 or 13
            if not (counter_y % 11 != 0 and counter_y % 13 != 0):
                fresh_agg.append(counter_y)
            helper_iterate(counter_y + 1)

    helper_iterate(0)

    fresh_cache: str = ""

    def build_string(idx: int) -> None:
        nonlocal fresh_cache
        if idx < len(fresh_agg):
            fresh_cache += str(fresh_agg[idx])
            build_string(idx + 1)

    build_string(0)

    fresh_count: int = 0
    for char_p in fresh_cache:
        if char_p == '7':
            fresh_count += 1

    return fresh_count