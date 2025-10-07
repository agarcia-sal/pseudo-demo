from typing import List

def is_nested(string: str) -> bool:
    def loop_through(i: int, op_idx: List[int], cl_idx: List[int], pos: int, cnt: int) -> bool:
        if i == len(op_idx):
            return cnt >= 2
        current_op_index = op_idx[i]
        if pos < len(cl_idx) and current_op_index < cl_idx[pos]:
            return loop_through(i + 1, op_idx, cl_idx, pos + 1, cnt + 1)
        else:
            return loop_through(i + 1, op_idx, cl_idx, pos, cnt)

    open_indices: List[int] = []
    close_indices: List[int] = []

    def gather_indices(idx: int) -> None:
        if idx == len(string):
            return
        if string[idx] == '[':
            open_indices.append(idx)
        else:
            close_indices.append(idx)
        gather_indices(idx + 1)

    gather_indices(0)
    close_indices.reverse()
    return loop_through(0, open_indices, close_indices, 0, 0)