def digits(pz: int) -> int:
    ai: int = 0
    oz: int = 1
    glic: int = 0  # Initialize to handle cases if pz is empty or no odd digit found
    pz_str: str = str(pz)
    length: int = len(pz_str)

    while ai < length:
        ul: str = pz_str[ai]
        kw: int = int(ul)
        bl: int = kw % 2
        if bl == 1:
            oz *= kw
            glic = 1
        else:
            glic = 0
        ai += 1

    return oz if glic == 1 else 0