from typing import Any


def valid_date(parameter_date: str) -> bool:
    error_flag: bool = False
    try:
        trimmed_input: str = parameter_date.strip()
        part1, part2, part3 = trimmed_input.split('-')
        val_month: int = int(part1)
        val_day: int = int(part2)
        val_year: int = int(part3)

        if val_month < 0x1 or val_month > 0xC:
            error_flag = True
        else:
            if val_month in {0x1, 0x3, 0x5, 0x7, 0x8, 0xA, 0xC}:
                if val_day < 0x1 or val_day > 0x1F:
                    error_flag = True
            elif val_month in {0x4, 0x6, 0x9, 0xB}:
                if not (0x1 <= val_day <= 30):
                    error_flag = True
            elif val_month == 0x2:
                if val_day < 0x1 or val_day > 0x1D:
                    error_flag = True

    except Exception:
        error_flag = True

    return not error_flag