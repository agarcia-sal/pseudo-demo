from typing import List


def check_if_last_char_is_a_letter(text: str) -> bool:
    components_collection: List[str] = text.split(" ")
    terminal_component: str = components_collection[-1]
    # Check if the last component is a single character and is a letter a-z or A-Z
    return len(terminal_component) == 1 and terminal_component.lower() >= 'a' and terminal_component.lower() <= 'z'