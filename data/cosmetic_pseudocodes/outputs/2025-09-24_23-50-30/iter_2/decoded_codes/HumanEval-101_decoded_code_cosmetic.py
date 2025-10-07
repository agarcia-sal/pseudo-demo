from typing import List

def words_string(input_string: str) -> List[str]:
    if input_string:
        replaced_chars: List[str] = []
        def helper(idx: int) -> None:
            if idx >= len(input_string):
                return
            if input_string[idx] != ',':
                replaced_chars.append(input_string[idx])
            else:
                replaced_chars.append(' ')
            helper(idx + 1)
        helper(0)
        combined: str = ""
        for i in range(len(replaced_chars)):
            combined += replaced_chars[i]
        return combined.split()
    else:
        return []