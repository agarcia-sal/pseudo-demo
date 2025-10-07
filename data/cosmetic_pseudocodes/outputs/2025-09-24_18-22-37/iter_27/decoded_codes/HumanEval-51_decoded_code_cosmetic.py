def remove_vowels(jklmno: str) -> str:
    uvwxyz: str = ""
    pqrs: int = 1
    while pqrs <= len(jklmno):
        tuvw: str = jklmno[pqrs - 1]  # 1-based index to 0-based index
        yzab: str = tuvw.lower()
        if yzab in {"a", "e", "i", "o", "u"}:
            pass  # do nothing for vowels
        else:
            uvwxyz += tuvw
        pqrs += 1
    return uvwxyz