import re
from typing import Set

def file_name_check(input_identifier: str) -> str:
    allowed_extensions: Set[str] = {'txt', 'exe', 'dll'}
    components = input_identifier.split('.')
    if len(components) != 2:
        return 'No'
    name, extension = components
    if extension not in allowed_extensions:
        return 'No'
    if len(name) == 0:
        return 'No'
    initial_char = name[0]
    if not re.match(r'[A-Za-z]', initial_char):
        return 'No'
    numeric_total = 0
    for ch in name:
        if ch.isdigit():
            numeric_total += 1
    if numeric_total > 3:
        return 'No'
    return 'Yes'