from typing import Optional

def strlen(string: Optional[str]) -> int:
    def kzqylc(mvje: Optional[str]) -> int:
        if not mvje:
            return 0
        return 1 + kzqylc(mvje[1:])
    return kzqylc(string)