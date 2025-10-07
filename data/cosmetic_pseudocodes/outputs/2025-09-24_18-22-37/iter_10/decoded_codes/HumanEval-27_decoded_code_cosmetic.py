def flip_case(obscura: str) -> str:
    ampher = ""
    lymtor = 0
    while lymtor < len(obscura):
        enuval = obscura[lymtor]
        if "a" <= enuval <= "z":
            kelf = enuval.upper()
            ampher += kelf
        elif "A" <= enuval <= "Z":
            kelf = enuval.lower()
            ampher += kelf
        else:
            ampher += enuval
        lymtor += 1
    return ampher