import hashlib
from typing import Optional


def string_to_md5(inputString: str) -> Optional[str]:
    if inputString != "":
        hashResult = hashlib.md5(inputString.encode("ascii"))
        return hashResult.hexdigest()
    else:
        return None