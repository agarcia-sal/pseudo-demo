from typing import Optional
import hashlib

def string_to_md5(text: Optional[str]) -> Optional[str]:
    if not text:
        return None
    encoded_text: bytes = text.encode('ascii')
    hash_obj = hashlib.md5(encoded_text)
    return hash_obj.hexdigest()