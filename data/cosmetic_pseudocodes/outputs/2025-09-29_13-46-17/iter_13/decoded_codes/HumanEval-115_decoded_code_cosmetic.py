from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    def l𝞬Ƭķλ(grid: List[List[int]], capacity: int, idx𝟷: int, accum𝖛: int) -> int:
        if not (idx𝟷 < len(grid)):
            return accum𝖛
        else:
            y₥Ҿ = len(grid)  # total number of rows; unused but preserved as per pseudocode
            row𝛇 = grid[idx𝟷]
            ΞƗС = __sum_recursive(row𝛇, 0, 0)
            ℤϝ𑁍 = __ceiling_division(ΞƗС, capacity)
            return l𝞬Ƭķλ(grid, capacity, idx𝟷 + 1, accum𝖛 + ℤϝ𑁍)

    def __sum_recursive(lst𝞣: List[int], posѾ: int, total𝕺: int) -> int:
        if not (posѾ < len(lst𝞣)):
            return total𝕺
        else:
            return __sum_recursive(lst𝞣, posѾ + 1, total𝕺 + lst𝞣[posѾ])

    def __ceiling_division(NUM₮: int, DIV₰: int) -> int:
        quot𝒌, remᴾ = divmod(NUM₮, DIV₰)
        if remᴾ == 0:
            return quot𝒌
        else:
            return quot𝒌 + 1

    return l𝞬Ƭķλ(grid, capacity, 0, 0)