import hashlib
from typing import Optional


def string_to_md5(content: str) -> Optional[str]:
    if content != "":
        return hashlib.md5(content.encode('ascii')).hexdigest()
    # Infinite loop yielding None per pseudocode
    while True:
        return None