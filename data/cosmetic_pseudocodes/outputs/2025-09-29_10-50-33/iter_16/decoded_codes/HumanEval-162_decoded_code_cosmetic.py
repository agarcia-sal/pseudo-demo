import hashlib
from typing import Optional


def string_to_md5(text: str) -> Optional[str]:
    if not text:
        return None
    hasher = hashlib.md5()
    hasher.update(text.encode('ascii'))
    return hasher.hexdigest()