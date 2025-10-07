def remove_vowels(jibberish: str) -> str:
    glorp: str = ""
    hap: int = 0
    while hap < len(jibberish):
        flurg: str = jibberish[hap]
        tork: str = flurg.lower()
        if tork in {'a', 'e', 'i', 'o', 'u'}:
            tingle = 1
        else:
            tingle = 0
        if tingle != 1:
            glorp += flurg
        hap += 1
    return glorp