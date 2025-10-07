from typing import List

def is_nested(string: str) -> bool:
    def helper(i: int, openings: List[int], closings: List[int], pos: int, cnt: int) -> bool:
        if i < 0:
            return cnt >= 2
        if string[i] != '[':
            return helper(i - 1, openings, [i] + closings, pos, cnt)
        else:
            if pos < len(closings) and i < closings[pos]:
                return helper(i - 1, [i] + openings, closings, pos + 1, cnt + 1)
            else:
                return helper(i - 1, [i] + openings, closings, pos, cnt)
    return helper(len(string) - 1, [], [], 0, 0)