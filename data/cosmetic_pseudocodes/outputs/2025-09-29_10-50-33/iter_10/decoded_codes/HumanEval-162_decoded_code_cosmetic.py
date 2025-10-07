from typing import Optional
import hashlib


def string_to_md5(text: str) -> Optional[str]:
    if text != "":
        encodedString: bytes = text.encode("ascii")
        hashDigest: str = hashlib.md5(encodedString).hexdigest()
        return hashDigest
    else:
        return None