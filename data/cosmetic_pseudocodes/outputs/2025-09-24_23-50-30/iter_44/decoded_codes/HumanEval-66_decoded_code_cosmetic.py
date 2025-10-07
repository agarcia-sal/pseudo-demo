def digitSum(text_value: str) -> int:
    if text_value == "":
        return 0
    return sum((ord(element) if 65 <= ord(element) <= 90 else 0) for element in text_value)