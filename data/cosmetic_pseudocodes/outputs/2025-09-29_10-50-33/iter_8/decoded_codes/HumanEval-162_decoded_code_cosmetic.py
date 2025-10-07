from typing import Optional
import hashlib

def string_to_md5(data_string: str) -> Optional[str]:
    def hash_generator(input_value: str) -> str:
        return hashlib.md5(input_value.encode('ascii')).hexdigest()

    while True:
        if data_string == "":
            return None
        else:
            return hash_generator(data_string)