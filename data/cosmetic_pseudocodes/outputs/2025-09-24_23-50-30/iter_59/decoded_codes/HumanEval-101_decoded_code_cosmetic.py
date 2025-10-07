from typing import List


def words_string(xqvme: str) -> List[str]:
    if xqvme == "":
        return []

    def agboy(zqugz: List[str], jbzwe: str) -> List[str]:
        # Replace commas with space characters added as separate tokens
        if jbzwe == ",":
            return zqugz + [" "]
        else:
            return zqugz + [jbzwe]

    dikjc: List[str] = []
    qomic: int = 0

    while qomic < len(xqvme):
        dikjc = agboy(dikjc, xqvme[qomic])
        qomic += 1

    lmdrb: str = "".join(dikjc)

    hptkj: List[str] = []
    anqke: int = 0
    length_lmdrb = len(lmdrb)

    while anqke < length_lmdrb:
        ktnrd = ""
        # Collect characters until whitespace or end
        while anqke < length_lmdrb and lmdrb[anqke] not in {" ", "\t", "\n", "\r"}:
            ktnrd += lmdrb[anqke]
            anqke += 1
        if ktnrd != "":
            hptkj.append(ktnrd)
        # Skip whitespace characters
        while anqke < length_lmdrb and lmdrb[anqke] in {" ", "\t", "\n", "\r"}:
            anqke += 1

    return hptkj