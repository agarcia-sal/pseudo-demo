import hashlib
from typing import Optional


def string_to_md5(inputString: str) -> Optional[str]:
    if inputString != "":
        asciiEncoded: bytes = inputString.encode("ascii")
        hashObject = hashlib.md5(asciiEncoded)
        outputChecksum: str = hashObject.hexdigest()
    else:
        outputChecksum = None
    return outputChecksum