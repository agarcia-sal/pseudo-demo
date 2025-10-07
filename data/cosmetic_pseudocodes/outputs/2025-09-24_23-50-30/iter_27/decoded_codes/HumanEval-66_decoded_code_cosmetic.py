def digitSum(text_param: str) -> int:
    if text_param == "":
        return 0

    aggregate_value: int = 0
    idx: int = 0
    while idx < len(text_param):
        elem: str = text_param[idx]
        if "A" <= elem <= "Z":
            aggregate_value += ord(elem)
        else:
            aggregate_value += 0
        idx += 1

    return aggregate_value