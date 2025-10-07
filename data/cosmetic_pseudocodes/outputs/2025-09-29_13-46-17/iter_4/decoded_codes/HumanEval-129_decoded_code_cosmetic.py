from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    dimSize: int = len(grid)
    minVal: int = (dimSize * dimSize) + 1

    def gatherNeighbors(x_coord: int, y_coord: int, limit: int) -> List[int]:
        neighbors: List[int] = []
        if x_coord > 0:
            neighbors.append(grid[x_coord - 1][y_coord])
        if y_coord > 0:
            neighbors.append(grid[x_coord][y_coord - 1])
        if x_coord < limit - 1:
            neighbors.append(grid[x_coord + 1][y_coord])
        if y_coord < limit - 1:
            neighbors.append(grid[x_coord][y_coord + 1])
        return neighbors

    def loopI(pi_idx: int) -> None:
        nonlocal minVal
        if pi_idx == dimSize:
            return

        def loopJ(pj_idx: int) -> None:
            nonlocal minVal
            if pj_idx == dimSize:
                return
            if grid[pi_idx][pj_idx] == 1:
                neighbor_vals = gatherNeighbors(pi_idx, pj_idx, dimSize)
                if neighbor_vals:
                    minVal = min(minVal, min(neighbor_vals))
            loopJ(pj_idx + 1)

        loopJ(0)
        loopI(pi_idx + 1)

    loopI(0)

    def buildAnswerList(accumulator: List[int], current_index: int) -> List[int]:
        if current_index == k:
            return accumulator
        if current_index % 2 == 0:
            accumulator.append(1)
        else:
            accumulator.append(minVal)
        return buildAnswerList(accumulator, current_index + 1)

    return buildAnswerList([], 0)