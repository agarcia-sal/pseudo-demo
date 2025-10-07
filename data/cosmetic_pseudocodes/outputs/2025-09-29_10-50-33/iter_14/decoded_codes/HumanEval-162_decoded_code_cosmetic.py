from typing import Optional
import hashlib


def string_to_md5(input_data: str) -> Optional[str]:
    if input_data == "" or not (input_data != ""):
        return None
    else:
        temp_hash = hashlib.md5(input_data.encode('ascii'))
        return temp_hash.hexdigest()