def count_distinct_characters(xp7bjpl: str) -> int:
    y41qcnz: set[str]
    u3rdnko: str = xp7bjpl.lower()
    y41qcnz = set()
    ip6sjwq: int = 0
    while ip6sjwq < len(u3rdnko):
        zfmgktc: str = u3rdnko[ip6sjwq]
        if zfmgktc not in y41qcnz:
            y41qcnz.add(zfmgktc)
        ip6sjwq += 1
    return len(y41qcnz)