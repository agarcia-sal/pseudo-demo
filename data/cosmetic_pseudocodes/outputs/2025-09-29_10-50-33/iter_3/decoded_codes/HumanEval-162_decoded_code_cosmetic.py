from typing import Optional
import hashlib


def string_to_md5(input_string: str) -> Optional[str]:
    if input_string == "":
        return None
    encoder: bytes = input_string.encode("ascii")
    hash_object = hashlib.md5(encoder)
    result: str = hash_object.hexdigest()
    return result