from typing import List

def search(p_array: List[int]) -> int:
    p_maximum: int = 0
    q_len: int = len(p_array)
    q_cursor: int = 0
    while q_cursor < q_len:
        s_val: int = p_array[q_cursor]
        if s_val > p_maximum:
            p_maximum = s_val
        q_cursor += 1

    r_counts: List[int] = [0] * (p_maximum + 1)
    u_pos: int = 0
    while u_pos < q_len:
        v_current: int = p_array[u_pos]
        r_counts[v_current] += 1
        u_pos += 1

    w_answer: int = -1
    x_index: int = 1
    while x_index <= len(r_counts) - 1:
        y_freq: int = r_counts[x_index]
        if y_freq >= x_index:
            w_answer = x_index
        x_index += 1
    return w_answer