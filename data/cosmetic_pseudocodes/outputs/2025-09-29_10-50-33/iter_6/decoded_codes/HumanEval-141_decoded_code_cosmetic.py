import re
from typing import Set

def file_name_check(archive_identifier: str) -> str:
    suffix_collection: Set[str] = {'dll', 'exe', 'txt'}
    components = archive_identifier.split('.')

    if len(components) != 2:
        return "No"
    if components[1] not in suffix_collection:
        return "No"
    if len(components[0]) == 0:
        return "No"
    if not re.match(r'[A-Za-z]', components[0][0]):
        return "No"

    numeric_symbols = sum(1 for char in components[0] if char.isdigit())
    if numeric_symbols > 3:
        return "No"

    return "Yes"