from collections import deque
from typing import List

def parse_nested_parens(parens_input: str) -> List[int]:
    def parse_paren_group(group_seq: str) -> int:
        depth_counter: int = 0
        max_depth_val: int = 0
        idx: int = 0
        while idx < len(group_seq):
            char_curr: str = group_seq[idx]
            if char_curr == '(':
                depth_counter += 1
                if max_depth_val < depth_counter:
                    max_depth_val = depth_counter
            else:
                depth_counter -= 1
            idx += 1
        return max_depth_val

    parts_queue: deque[str] = deque()
    for ch in parens_input:
        if ch == ' ':
            parts_queue.append('')
        else:
            if not parts_queue:
                parts_queue.append(ch)
            else:
                last_str = parts_queue.pop()
                parts_queue.append(last_str + ch)

    results_list: List[int] = []
    while parts_queue:
        segment = parts_queue.popleft()
        if segment:
            results_list.append(parse_paren_group(segment))

    return results_list