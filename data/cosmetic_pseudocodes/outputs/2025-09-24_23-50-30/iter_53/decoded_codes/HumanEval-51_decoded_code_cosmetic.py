def remove_vowels(xqrmv: str) -> str:
    yslip = ""
    zkebf = 0
    vowels = {"a", "e", "i", "o", "u"}
    while zkebf < len(xqrmv):
        tcast = xqrmv[zkebf]
        if tcast.lower() not in vowels:
            yslip += tcast
        zkebf += 1
    return yslip