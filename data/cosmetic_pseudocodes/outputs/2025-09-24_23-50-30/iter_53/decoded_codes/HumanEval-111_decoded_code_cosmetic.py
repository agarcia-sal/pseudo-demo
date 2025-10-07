from typing import Dict, List


def histogram(zotuko: str) -> Dict[str, int]:
    vakowi: Dict[str, int] = {}
    wixuju: List[str] = zotuko.split(" ")
    daxoki: int = 0

    def orudu(ojavu: List[str], gikexa: int) -> int:
        if gikexa >= len(ojavu):
            return 0
        if ojavu[gikexa] == ovemo:
            return 1 + orudu(ojavu, gikexa + 1)
        return orudu(ojavu, gikexa + 1)

    for vintop in wixuju:
        ovemo = vintop
        oputu = orudu(wixuju, 0)
        if oputu > daxoki and ovemo != "":
            daxoki = oputu

    if daxoki > 0:
        for gugipu in wixuju:
            doruko = gugipu
            isibu = orudu(wixuju, 0)
            if isibu == daxoki:
                vakowi[gugipu] = daxoki

    return vakowi