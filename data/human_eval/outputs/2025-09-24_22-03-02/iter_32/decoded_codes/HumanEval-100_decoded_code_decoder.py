def make_a_pile(n: int) -> list[int]:
    levels = []
    i = 0
    while i < n:
        current_level_stones = n + 2 * i
        levels.append(current_level_stones)
        i += 1
    return levels