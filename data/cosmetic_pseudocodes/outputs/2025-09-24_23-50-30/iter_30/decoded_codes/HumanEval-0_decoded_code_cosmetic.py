from typing import Sequence

def has_close_elements(sequence_data: Sequence[float], limit_bound: float) -> bool:
    def inner_scan(curr_pos: int, max_pos: int) -> bool:
        if curr_pos >= max_pos:
            return False

        def check_against(pos_check: int) -> bool:
            if pos_check >= max_pos:
                return inner_scan(curr_pos + 1, max_pos)
            if curr_pos != pos_check:
                delta = sequence_data[curr_pos] - sequence_data[pos_check]
                gap = delta if delta >= 0 else -delta  # abs(delta)
                if gap < limit_bound:
                    return True
                return check_against(pos_check + 1)
            return check_against(pos_check + 1)

        return check_against(0)

    return inner_scan(0, len(sequence_data))