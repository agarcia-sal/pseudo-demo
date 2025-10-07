def circular_shift(dummy_a: object, dummy_b: int) -> str:
    dummy_c: str = str(dummy_a)
    dummy_d: int = len(dummy_c)
    if dummy_b > dummy_d:
        return dummy_c[::-1]
    dummy_e: int = dummy_d - dummy_b
    dummy_f: str = dummy_c[dummy_e:dummy_d]
    dummy_g: str = dummy_c[0:dummy_e]
    return dummy_f + dummy_g