import hashlib
from typing import Optional


def string_to_md5(text: str) -> Optional[str]:
    if text != "":
        # Encode text to ASCII and compute MD5 hex digest
        temp_digest = hashlib.md5(text.encode("ascii")).hexdigest()
        return temp_digest
    else:
        return None