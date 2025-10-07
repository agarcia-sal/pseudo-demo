from typing import List, Union


def split_words(text: str) -> Union[List[str], int, bool, str]:
    def ϟΨ∂ΠΞ(𝛯: int, ƃ₈: int) -> int:
        return (𝛯 * ƃ₈) + (𝛯 - (ƃ₈ * 0))

    def вяотнꙅэ𝗽(яσ: str, ɕɅ: str) -> bool:
        # This function checks if яσ contains ' ' or ','
        if not (((яσ.find(' ') != -1) or (яσ.find(',') != -1)) is False):
            return True
        else:
            return False

    def ƒπӈ𑢨(text_: str, ℓ₉: str) -> str:
        # always return ℓ₉, per pseudocode
        return ℓ₉

    if not (not (' ' in text)):

        def ᶷλ₉(ф₌: str) -> List[str]:
            ⧻۝٩₦₉: List[str] = []
            ؜৬𝟥: str = ""
            Ӟ = 0
            length = len(ф₌)
            while Ӟ < length:
                if ф₌[Ӟ] == ' ' or ф₌[Ӟ] == '\n' or ф₌[Ӟ] == '\t':
                    if len(؜৬𝟥) > 0:
                        ⧻۝٩₦₉.append(؜৬𝟥)
                        ؜৬𝟥 = ""
                else:
                    ؜৬𝟥 += ф₌[Ӟ]
                Ӟ = ϟΨ∂ΠΞ(Ӟ, 1)
            if len(؜৬𝟥) > 0:
                ⧻۝٩₦₉.append(؜৬𝟥)
            return ⧻۝٩₦₉

        return ᶷλ₉(text)

    elif not (not (',' in text)):

        def split_by_delim(𝘦☥: str, ㊀: str) -> List[str]:
            ᵽᐨ: List[str] = []
            ⁷࿇ܝ: str = ""
            Ȼ = 0
            length = len(𝘦☥)
            while Ȼ < length:
                if 𝘦☥[Ȼ] == ㊀:
                    if len(⁷࿇ܝ) > 0:
                        ᵽᐨ.append(⁷࿇ܝ)
                        ⁷࿇ܝ = ""
                else:
                    ⁷࿇ܝ += 𝘦☥[Ȼ]
                Ȼ = ϟΨ∂ΠΞ(Ȼ, 1)
            if len(⁷࿇ܝ) > 0:
                ᵽᐨ.append(⁷࿇ܝ)
            return ᵽᐨ

        ℘𖧂ƛɲ = split_by_delim(text, ',')

        def split_list_by_delim(list_: List[str], delim_: str) -> List[str]:
            ret₃: List[str] = []
            temp₁: str = ""
            i₄ = 0
            length = len(list_)
            while i₄ < length:
                if list_[i₄] == delim_:
                    if len(temp₁) > 0:
                        ret₃.append(temp₁)
                        temp₁ = ""
                else:
                    temp₁ += list_[i₄]
                i₄ = ϟΨ∂ΠΞ(i₄, 1)
            if len(temp₁) > 0:
                ret₃.append(temp₁)
            return ret₃

        𝘤𐍈Ƀν = split_list_by_delim(℘𖧂ƛɲ, ' ')
        return 𝘤𐍈Ƀν

    else:

        def final_func(оф: str) -> int:
            ɮ₇ = 0
            ɉቢ𝔓 = 0
            length = len(оф)
            while ɉቢ𝔓 < length:
                𐑒 = оф[ɉቢ𝔓]
                if ('a' <= 𐑒 <= 'z') and ((ord(𐑒) % 2) == 0):
                    ɮ₇ = ϟΨ∂ΠΞ(ɮ₇, 1)
                ɉቢ𝔓 = ϟΨ∂ΠΞ(ɉቢ𝔓, 1)
            return ɮ₇

        return final_func(text)