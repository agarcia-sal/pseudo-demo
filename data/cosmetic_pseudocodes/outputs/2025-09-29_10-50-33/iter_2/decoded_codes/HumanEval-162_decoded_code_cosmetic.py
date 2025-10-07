from typing import Optional
import hashlib


def string_to_md5(input_string: str) -> Optional[str]:
    if len(input_string) > 0:
        hash_value = hashlib.md5(input_string.encode('ascii'))
        return hash_value.hexdigest()
    else:
        return None