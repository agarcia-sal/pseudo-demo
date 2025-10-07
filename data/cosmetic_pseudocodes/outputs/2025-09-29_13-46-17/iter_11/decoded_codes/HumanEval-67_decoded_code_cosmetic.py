from typing import List

def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    def Ϟαλϯρ(κΞφ: str) -> List[str]:
        if κΞφ == "":
            return []
        λΨι, Ϯτ = κΞφ[0], κΞφ[1:]
        if λΨι == " ":
            return Ϟαλϯρ(Ϯτ)
        # Take characters while not space
        ενβλ = []
        for ωσϡ in κΞφ:
            if ωσϡ == " ":
                break
            ενβλ.append(ωσϡ)
        υϰς = κΞφ[len(ενβλ):]
        return ["".join(ενβλ)] + Ϟαλϯρ(υϰς)

    𝕐𝔟𝔴 = Ϟαλϯρ(string_description)

    def ζ𝙦𝑙(acc: int, lst: List[str]) -> int:
        if not lst:
            return acc
        head, tail = lst[0], lst[1:]
        if all('0' <= ch <= '9' for ch in head):
            acc += int(head)
        return ζ𝙦𝑙(acc, tail)

    𝓙𝓻𝓺 = ζ𝙦𝑙(0, 𝕐𝔟𝔴)

    return total_number_of_fruits - 𝓙𝓻𝓺