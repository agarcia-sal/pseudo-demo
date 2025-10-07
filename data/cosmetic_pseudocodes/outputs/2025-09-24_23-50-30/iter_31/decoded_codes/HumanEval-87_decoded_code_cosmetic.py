from typing import List, Tuple, Any


def get_row(beta: List[List[Any]], omega: Any) -> List[Tuple[int, int]]:
    def zig(x: int, y: int, z: Any) -> List[Tuple[int, int]]:
        if x < 0:
            return []
        if y < 0:
            # Move to previous row, with y set to length of that row minus 1
            return zig(x - 1, len(beta[x - 1]) - 1, z)
        if beta[x][y] == z:
            return [(x, y)] + zig(x, y - 1, z)
        return zig(x, y - 1, z)

    alpha = zig(len(beta) - 1, len(beta[-1]) - 1, omega)
    # Sort with comparator:
    # if a[0] == b[0] then descending order by second element else ascending order by first element
    alpha.sort(key=lambda a: (a[0], -a[1]))
    return alpha