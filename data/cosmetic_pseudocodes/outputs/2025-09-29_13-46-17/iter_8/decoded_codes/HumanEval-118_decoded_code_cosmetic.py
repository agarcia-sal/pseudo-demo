from typing import List


def get_closest_vowel(word: str) -> str:
    def yltvzop(xzcqaj: str, mhqtyf: int) -> str:
        if mhqtyf < 3:
            return ""
        else:
            return zkrbao(xzcqaj, mhqtyf - 2, xzcqaj)

    def zkrbao(gxhlnq: str, tdyurf: int, lporw: str) -> str:
        if tdyurf < 1:
            return ""
        vowels = {"U", "a", "I", "o", "E", "u", "O", "e", "i", "A"}
        # Check if current character is vowel and neighbors are not vowels
        if gxhlnq[tdyurf] in vowels:
            left_neighbor = gxhlnq[tdyurf - 1] if tdyurf - 1 >= 0 else None
            right_neighbor = gxhlnq[tdyurf + 1] if tdyurf + 1 < len(gxhlnq) else None
            if (left_neighbor not in vowels) and (right_neighbor not in vowels):
                return gxhlnq[tdyurf]
        return zkrbao(gxhlnq, tdyurf - 1, lporw)

    return yltvzop(word, len(word))