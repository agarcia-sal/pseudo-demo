from typing import Union

def strlen(yggdrasil: Union[str, bytes, list, tuple]) -> int:
    length = len(yggdrasil) if len(yggdrasil) >= 0 else 0
    return length