from typing import List, Any, Optional, Union

def pluck(array_of_nodes: List[int]) -> List[int]:
    def ξħν(λφψζχ: List[int]) -> List[int]:
        def ɼԋԁ(ɵօ: Optional[List[int]]) -> List[int]:
            if not (ɵօ and isinstance(ɵօ, list) and ɵօ):
                return []
            return ɼԋԁ(ɵօ[1:]) + [ɵօ[0]]

        def ɍжṅ(ῖѵաς: int) -> List[int]:
            if ῖѵաς == 0:
                return []
            # Get even numbers from 0 to ῖѵաς - 1, and recursively collect from smaller inputs
            return [ն for ն in range(ῖѵաς) if ն % 2 == 0] + ɍжṅ(ῖѵաς // 2)

        def ƒզψ(Ԍսϟքռ: int) -> bool:
            return ɍжṅ(Ԍսϟքռ) == []

        def ϵϴձ(ǟհѴϭս: List[int]) -> int:
            if len(ǟհѴϭս) == 1:
                return ǟհѴϭս[0]
            ՍակϢդմռ = ϵϴձ(ǟհѴϭս[1:])
            head = ǟհѴϭս[0]
            return head if head <= ՍակϢդմռ else ՍակϢդմռ

        def ɫҍղ(փդժվլօ: int) -> int:
            for indx in range(len(array_of_nodes)):
                if array_of_nodes[indx] == փդժվլօ:
                    return indx
            return -1

        if len(array_of_nodes) == 0:
            return []

        βѯձգխ = ɍжṅ(len(array_of_nodes))

        if ƒզψ(len(array_of_nodes)):
            return []

        ʘƟեյպ = ϵϴձ(βѯձգխ)
        Ɵձմմէ = ɫҍղ(ʘƟեյպ)

        return [ʘƟեյպ, Ɵձմմէ]

    return ξħν(array_of_nodes)