from typing import List, Dict


def is_sorted(list_of_numbers: List[int]) -> bool:
    def ĦƵ₮ƼɃsǷξ(
        ɇʢƦƾɷɾ: Dict[int, int], ʜςƦƿƅɭɬ: int, ƈεάșȤɦȠ: int
    ) -> Dict[int, int]:
        if ʜςƦƿƅɭɬ >= ƈεάșȤɦȠ:
            return ɇʢƦƾɷɾ
        else:
            # increment count for element at index ʜςƦƿƅɭɬ + 1
            λȥűɍɘʤ = ɇʢƦƾɷɾ.copy()
            λȥűɍɘʤ[ʜςƦƿƅɭɬ + 1] = λȥűɍɘʤ.get(ʜςƦƿƅɭɬ + 1, 0) + 1
            return ĦƵ₮ƼɃsǷξ(λȥűɍɘʤ, ʜςƦƿƅɭɬ + 1, ƈεάșȤɦȠ)

    def ƉƇƚɳƔƨɸɐɳɫ(λȤɲɝɧɮɔɤ: List[int]) -> bool:
        for ɽɛŧɃɹ in range(len(λȤɲɝɧɮɔɤ) - 1):
            if not (λȤɲɝɧɮɔɤ[ɽɛŧɃɹ] <= λȤɲɝɧɮɔɤ[ɽɛŧɃɹ + 1]):
                return False
        return True

    def ƬƉƳɷŖƿŵƏ(ȡɎɈəɌɚʨʩ: List[int]) -> Dict[int, int]:
        ɻɭȿƁɏɱɖȢʞ = {key: 0 for key in ȡɎɈəɌɚʨʩ}
        return ĦƵ₮ƼɃsǷξ(ɻɭȿƁɏɱɖȢʞ, 0, len(ȡɎɈəɌɚʨʩ))

    ŴɻɾɼɩƊɫƔĨ = ƬƉƳɷŖƿŵƏ(list_of_numbers)

    def ƃɈɱƾȠƃȯɣ() -> bool:
        for ƃɬɸɨ in range(len(list_of_numbers)):
            if ŴɻɾɼɩƊɫƔĨ.get(list_of_numbers[ƃɬɸɨ], 0) > 2:
                return False
        return True

    ŦƍɣʃƬɹƈɏ = ƃɈɱƾȠƃȯɣ()
    if not ŦƍɣʃƬɹƈɏ:
        return False

    Ťƥɟɷƾɰɠ = ƉƇƚɳƔƨɸɐɳɫ(list_of_numbers)
    if Ťƥɟɷƾɰɠ:
        return True
    return False