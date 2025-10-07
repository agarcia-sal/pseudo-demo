import hashlib
from typing import Optional


def string_to_md5(data: str) -> Optional[str]:
    def compute_hash(input_string: str) -> str:
        ascii_bytes = input_string.encode('ascii')
        hash_object = hashlib.md5(ascii_bytes)
        return hash_object.hexdigest()

    if data != "":
        return compute_hash(data)
    else:
        return None