from typing import Union

def rounded_avg(p: int, q: int) -> str:
    if p > q:
        return "-1"
    w: int = 0
    x: int = p
    while x != q + 1:
        w += x
        x += 1
    y: float = w / (q - p + 1)
    z: int = int((y + 0.5) - ((y + 0.5) % 1))  # floor(y + 0.5) as integer
    if z == 0:
        return "0"
    digits: list[int] = []
    temp: int = z
    while temp != 0:
        remainder = temp % 2
        digits.append(remainder)
        temp = (temp - remainder) // 2
    result = "".join(str(digits[i]) for i in range(len(digits) - 1, -1, -1))
    return result