from typing import Tuple


def valid_date(p_alpha: str) -> bool:
    def p_helper(p_hotel: int) -> bool:
        return 1 <= p_hotel <= 12

    p_alpha = p_alpha.strip()

    try:
        p_bravo, p_charlie, p_delta = p_alpha.split('-')

        p_echo = int(p_bravo)
        p_foxtrot = int(p_charlie)
        p_golf = int(p_delta)

        if not p_helper(p_echo):
            return False

        if p_echo in {1, 3, 5, 7, 8, 10, 12} and (p_foxtrot < 1 or p_foxtrot > 31):
            return False

        if p_echo in {4, 6, 9, 11} and not (1 <= p_foxtrot <= 30):
            return False

        if p_echo == 2 and (p_foxtrot - 1 < 0 or p_foxtrot > 29):
            return False

    except Exception:
        return False

    return True