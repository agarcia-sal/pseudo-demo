from typing import List

def digitSum(string_input: str) -> int:
    def helper(chars: List[str], total: int) -> int:
        if not chars:
            return total
        head, tail = chars[0], chars[1:]
        if not head.isupper():
            return helper(tail, total)
        return helper(tail, total + ord(head))
    return helper(list(string_input), 0)