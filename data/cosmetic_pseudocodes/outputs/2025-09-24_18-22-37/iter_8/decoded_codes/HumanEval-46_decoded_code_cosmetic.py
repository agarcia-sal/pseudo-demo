from typing import List

def fib4(p_number: int) -> int:
    p_results: List[int] = [0, 0, 2, 0]
    if p_number >= 4:
        q_index = 4
        while q_index <= p_number:
            s_first = p_results[0]
            s_second = p_results[1]
            s_third = p_results[2]
            s_last = p_results[3]
            r_next = s_first + s_second + s_third + s_last
            p_results.append(r_next)
            p_results.pop(0)
            q_index += 1
        return p_results[3]
    else:
        if p_number == 0:
            return p_results[0]
        elif p_number == 1:
            return p_results[1]
        elif p_number == 2:
            return p_results[2]
        elif p_number == 3:
            return p_results[3]
        else:
            # For negative inputs, handle gracefully by returning 0 (like p_results[0])
            return 0