from typing import List

def strange_sort_list(list_of_integers: List[int]) -> List[int]:
    def helper(Λκζ: List[int], Ψβν: List[int], ζθξ: bool) -> List[int]:
        if Λκζ:
            if ζθξ:
                Μμτ = Λκζ[0]
                Νσφ = 0

                def finder(φρπ: List[int], 壹: int) -> List[int]:
                    if 壹 == len(φρπ):
                        return [Μμτ, Νσφ]
                    if φρπ[壹] < Μμτ:
                        nonlocal Μμτ, Νσφ
                        Μμτ = φρπ[壹]
                        Νσφ = 壹
                    return finder(φρπ, 壹 + 1)

                Μμτ, Νσφ = finder(Λκζ, 0)
                return helper(Λκζ[:Νσφ] + Λκζ[Νσφ + 1:], Ψβν + [Μμτ], not ζθξ)
            else:
                Πσδ = Λκζ[0]
                Ρυβ = 0

                def finder_max(φρπ: List[int], 壹: int) -> List[int]:
                    if 壹 == len(φρπ):
                        return [Πσδ, Ρυβ]
                    if φρπ[壹] > Πσδ:
                        nonlocal Πσδ, Ρυβ
                        Πσδ = φρπ[壹]
                        Ρυβ = 壹
                    return finder_max(φρπ, 壹 + 1)

                Πσδ, Ρυβ = finder_max(Λκζ, 0)
                return helper(Λκζ[:Ρυβ] + Λκζ[Ρυβ + 1:], Ψβν + [Πσδ], not ζθξ)
        return Ψβν

    return helper(list_of_integers, [], True)