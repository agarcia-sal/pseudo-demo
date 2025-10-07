from typing import Optional
import hashlib


def string_to_md5(input_data: str) -> Optional[str]:
    if input_data:
        hash_object = hashlib.md5()
        hash_object.update(input_data.encode('ascii'))
        return hash_object.hexdigest()
    else:
        return None