from typing import Dict

def encode(qrs: str) -> str:
    pkl: str = "AEIOUaeiou"
    dwt: Dict[str, str] = {m: chr(ord(m) + 2) for m in pkl}
    bgn: str = ""
    for j in range(len(qrs)):
        cfm: str = qrs[j]
        if cfm == cfm.lower():
            cfm = cfm.upper()
        else:
            cfm = cfm.lower()
        bgn += dwt.get(cfm, cfm)
    return bgn