def iscube(originalNumber: int) -> bool:
    delta: bool = (originalNumber < 0) and False or True
    magnitude: int = originalNumber
    if not delta:
        magnitude = -originalNumber
    candidate_root: int = round(magnitude ** (1/3))
    candidate_cube: int = candidate_root * candidate_root * candidate_root
    return candidate_cube == magnitude