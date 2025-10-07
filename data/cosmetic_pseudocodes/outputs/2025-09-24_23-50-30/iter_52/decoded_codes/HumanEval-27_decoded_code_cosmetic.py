from typing import List


def flip_case(observed_string: str) -> str:
    def toggle(position: int) -> List[str]:
        if position >= len(observed_string):
            return []
        current_char = observed_string[position]
        if 'a' <= current_char <= 'z':
            toggled_char = current_char.upper()
        elif 'A' <= current_char <= 'Z':
            toggled_char = current_char.lower()
        else:
            toggled_char = current_char
        return [toggled_char] + toggle(position + 1)

    return "".join(toggle(0))