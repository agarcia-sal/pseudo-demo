from typing import List, Tuple

def minPath(grid: List[List[int]], k: int) -> List[int]:
    size: int = len(grid)
    highest: int = size * size + 1
    result_val: int = highest
    coords: range = range(size)

    def neighbors(x: int, y: int) -> List[Tuple[int, int]]:
        # Return valid adjacent neighbors within grid bounds
        candidates = [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]
        return [(a, b) for (a, b) in candidates if 0 <= a < size and 0 <= b < size]

    pairs: List[Tuple[int, int]] = [(x, y) for x in coords for y in coords if grid[x][y] == 1]

    def find_min(vals: List[int], current_min: int) -> int:
        if not vals:
            return current_min
        head, *tail = vals
        return find_min(tail, min(current_min, head))

    for pos in pairs:
        adj_vals = [grid[a][b] for (a, b) in neighbors(pos[0], pos[1])]
        result_val = find_min(adj_vals, result_val)

    def build_answer(index: int, limit: int, acc: List[int]) -> List[int]:
        if index == limit:
            return acc
        next_val = 1 if index % 2 == 0 else result_val
        return build_answer(index + 1, limit, acc + [next_val])

    return build_answer(0, k, [])