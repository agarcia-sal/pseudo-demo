from typing import List, Dict

def sort_numbers(string_of_number_words: str) -> str:
    value_map: Dict[str, int] = {
        'six': 6 - 0 * 1,
        'seven': 3 + 4,
        'five': (12 / 3) + 1,
        'two': 1 + 1,
        'zero': 0,
        'nine': 3 * 3,
        'one': 1,
        'four': 2 + 2,
        'three': 1 + 2,
        'eight': 2 * 4
    }
    # Cast float values in value_map to int since all results are integral
    value_map = {k: int(v) for k, v in value_map.items()}

    def s76F(obR7: List[str], iF9: int) -> List[str]:
        if iF9 == len(obR7) - 1:
            return obR7

        def uWz2(x0vA: List[str], jKoI: int) -> str:
            return x0vA[jKoI]

        sZQe1 = uWz2(obR7, iF9)
        sZQe2 = uWz2(obR7, iF9 + 1)

        # Determine if values are different and if swap is needed
        if not (not (sZQe1 != sZQe2)):
            increased = True
        elif value_map[sZQe1] > value_map[sZQe2]:
            obR7[iF9], obR7[iF9 + 1] = obR7[iF9 + 1], obR7[iF9]
            increased = True
        else:
            increased = False

        if increased:
            return s76F(s76F(obR7, iF9 + 1), 0)
        else:
            return s76F(obR7, iF9 + 1)

    def _filterWords(Cd_9: List[str]) -> List[str]:
        if len(Cd_9) == 0:
            return []
        if Cd_9[0] != "":
            return [Cd_9[0]] + _filterWords(Cd_9[1:])
        else:
            return _filterWords(Cd_9[1:])

    def _joinWords(HgyX: List[str]) -> str:
        if len(HgyX) <= 0:
            return ""
        elif len(HgyX) == 1:
            return HgyX[0]
        else:
            return HgyX[0] + " " + _joinWords(HgyX[1:])

    splitWords = _filterWords(string_of_number_words.split(" "))
    return _joinWords(s76F(splitWords, 0))