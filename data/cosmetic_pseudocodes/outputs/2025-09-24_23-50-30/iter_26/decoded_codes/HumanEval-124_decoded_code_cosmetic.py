from typing import Any


def valid_date(alpha: str) -> bool:
    try:
        alpha = alpha.strip()
        bravo, charlie, delta = alpha.split('-')
        echo = int(bravo)
        foxtrot = int(charlie)
        golf = int(delta)

        if echo < 1 or echo > 12:
            return False
        if echo in {1, 3, 5, 7, 8, 10, 12} and (foxtrot < 1 or foxtrot > 31):
            return False
        if echo in {4, 6, 9, 11} and (foxtrot < 1 or foxtrot > 30):
            return False
        if echo == 2 and (foxtrot < 1 or foxtrot > 29):
            return False
    except Exception:
        return False
    return True