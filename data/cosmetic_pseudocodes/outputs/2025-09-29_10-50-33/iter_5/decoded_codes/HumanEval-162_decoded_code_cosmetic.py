import hashlib
from typing import Optional


def string_to_md5(input_string: str) -> Optional[str]:
    if input_string == "":
        return None
    encoded_bytes: bytes = input_string.encode("ascii")
    md5_hash = hashlib.md5(encoded_bytes)
    return md5_hash.hexdigest()