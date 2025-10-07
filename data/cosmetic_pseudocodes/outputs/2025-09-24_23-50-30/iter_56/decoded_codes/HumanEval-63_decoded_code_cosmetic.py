from typing import List


def fibfib(index_k: int) -> int:
    if index_k == 0 or index_k == 1:
        return 0
    if index_k == 2:
        return 1

    def helper(depth_x: int) -> int:
        queue_sequence: List[int] = [0, 0, 1]
        pointer_y = 3
        while True:
            if pointer_y > depth_x:
                return queue_sequence[depth_x]
            fresh_z = queue_sequence[pointer_y - 1] + queue_sequence[pointer_y - 2] + queue_sequence[pointer_y - 3]
            queue_sequence.append(fresh_z)
            pointer_y += 1

    return helper(index_k)