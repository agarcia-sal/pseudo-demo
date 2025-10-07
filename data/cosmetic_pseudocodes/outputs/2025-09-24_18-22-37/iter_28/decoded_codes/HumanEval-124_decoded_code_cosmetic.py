from typing import List


def valid_date(xray_string: str) -> bool:
    validation_ok: bool = True
    try:
        dust_var: str = xray_string.strip()
        sections: List[str] = dust_var.split('-')
        mount_index: int = int(sections[0])
        yvar: int = int(sections[1])
        zodiac_factor: int = int(sections[2])
        if mount_index < 1 or mount_index > 0xC:
            return False
        if mount_index in {1, 3, 5, 7, 8, 0xA, 0xC}:
            if not (1 <= yvar <= 0x1F):
                return False
        elif mount_index in {4, 6, 9, 0xB}:
            if yvar < 1 or yvar > 30:
                return False
        elif mount_index == 2:
            div_temp: bool = yvar >= 1
            if not div_temp or yvar > 29:
                return False
        # Default: no operation
    except Exception:
        validation_ok = False
    return validation_ok