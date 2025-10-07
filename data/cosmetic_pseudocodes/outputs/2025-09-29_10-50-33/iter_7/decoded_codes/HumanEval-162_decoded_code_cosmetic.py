from typing import Optional
import hashlib


def string_to_md5(input_sequence: str) -> Optional[str]:
    if not input_sequence:
        return None
    encoded_data: bytes = input_sequence.encode('ascii')
    digest_value: str = hashlib.md5(encoded_data).hexdigest()
    return digest_value