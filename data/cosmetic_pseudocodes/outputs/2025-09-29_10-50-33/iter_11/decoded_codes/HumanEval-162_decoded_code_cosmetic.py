from typing import Optional
import hashlib


def string_to_md5(inputData: str) -> Optional[str]:
    if inputData != "":
        return hashlib.md5(inputData.encode('ascii')).hexdigest()
    else:
        return None