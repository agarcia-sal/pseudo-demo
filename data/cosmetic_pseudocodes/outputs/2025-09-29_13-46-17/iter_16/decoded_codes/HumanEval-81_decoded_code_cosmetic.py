from typing import List, Set

def numerical_letter_grade(list_of_grades: List[float]) -> Set[str]:
    def ꜰθλ(𝕧𝓇𝕩𝟛𝓉: Set[str], 𝕜𝓥: List[float]) -> Set[str]:
        def 𝕓𝖆𝓅𝕝(𝓇𝔷𝔲𝕙: float) -> None:
            k = 𝓇𝔷𝔲𝕙
            if k == 4.0:
                𝕧𝓇𝕩𝟛𝓉.add("A+")
            elif k > 3.7:
                𝕧𝓇𝕩𝟛𝓉.add("A")
            elif k > 3.3:
                𝕧𝓇𝕩𝟛𝓉.add("A-")
            elif k > 3.0:
                𝕧𝓇𝕩𝟛𝓉.add("B+")
            elif k > 2.7:
                𝕧𝓇𝕩𝟛𝓉.add("B")
            elif k > 2.3:
                𝕧𝓇𝕩𝟛𝓉.add("B-")
            elif k > 2.0:
                𝕧𝓇𝕩𝟛𝓉.add("C+")
            elif k > 1.7:
                𝕧𝓇𝕩𝟛𝓉.add("C")
            elif k > 1.3:
                𝕧𝓇𝕩𝟛𝓉.add("C-")
            elif k > 1.0:
                𝕧𝓇𝕩𝟛𝓉.add("D+")
            elif k > 0.7:
                𝕧𝓇𝕩𝟛𝓉.add("D")
            elif k > 0.0:
                𝕧𝓇𝕩𝟛𝓉.add("D-")
            else:
                𝕧𝓇𝕩𝟛𝓉.add("E")

        if 𝕜𝓥:
            HEAD = 𝕜𝓥[0]
            TAIL = 𝕜𝓥[1:]
            𝕓𝖆𝓅𝕝(HEAD)
            return ꜰθλ(𝕧𝓇𝕩𝟛𝓉, TAIL)
        else:
            return 𝕧𝓇𝕩𝟛𝓉

    return ꜰθλ(set(), list_of_grades)