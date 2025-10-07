from typing import Optional
import hashlib

def string_to_md5(text: str) -> Optional[str]:
    if text:
        return hashlib.md5(text.encode('ascii')).hexdigest()
    return None