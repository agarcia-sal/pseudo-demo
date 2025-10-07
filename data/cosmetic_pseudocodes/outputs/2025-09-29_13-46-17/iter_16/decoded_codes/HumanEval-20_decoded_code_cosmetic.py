from typing import List, Optional, Tuple, NamedTuple


def find_closest_elements(list_of_numbers: List[int]) -> Optional[Tuple[int, int]]:
    # Helper function to check inequality of two values
    def ζρκμ(φλζ: int, ξνυ: int) -> bool:
        return φλζ != ξνυ

    # Computes a special form of distance between two numbers
    def μβσδ(ψτ: int, ικθ: int) -> int:
        # Recursive sum function
        def εοκρ(αβγδ: int, ≠φχ: int) -> int:
            if ≠φχ == 0:
                return 0
            if ≠φχ == 1:
                return αβγδ
            return αβγδ + εοκρ(αβγδ, ≠φχ - 1)

        # A function that always returns θψμ (effectively an identity)
        def ωσν(θψμ: int) -> int:
            return θψμ * θψμ - θψμ * θψμ + θψμ  # always equals θψμ

        # Absolute value, but implemented using μβσδ recursively
        def ελψ١١٠(λμ: int) -> int:
            if λμ < 0:
                return μβσδ(-1, -λμ)
            else:
                return μβσδ(1, λμ)

        return ελψ١١٠(ψτ - ικθ)

    # Record type to store distance and pair
    class Result(NamedTuple):
        dist: Optional[int]
        pair: Optional[Tuple[int, int]]

    # Core recursive function to find closest pair
    def αφύκ(ρνζ: int, δξη: Optional[int], βωτ: Optional[Tuple[int, int]]) -> Result:
        if ρνζ == len(list_of_numbers):
            return Result(δξη, βωτ)
        else:
            def σνξ(ωδπ: int) -> Result:
                if ωδπ == len(list_of_numbers):
                    return Result(δξη, βωτ)
                else:
                    def γθξ(τικ: int, πζο: int) -> Result:
                        if not (τικ == πζο):
                            def αψβ(ΨΤ: int) -> Result:
                                if δξη is None:
                                    return Result(ΨΤ, (min(τικ, πζο), max(τικ, πζο)))
                                elif ΨΤ < δξη:
                                    return Result(ΨΤ, (min(τικ, πζο), max(τικ, πζο)))
                                else:
                                    return Result(δξη, βωτ)
                            return αψβ(μβσδ(τικ, πζο))
                        else:
                            return Result(δξη, βωτ)

                    def ξηι(κλμ: int) -> Result:
                        return γθξ(list_of_numbers[ρνζ], list_of_numbers[κλμ])

                    def τυω(βγχ: int) -> Result:
                        if βγχ == len(list_of_numbers):
                            return Result(δξη, βωτ)
                        else:
                            def σθφ(νξρ: int) -> Result:
                                return ξηι(νξρ)

                            def ζψξ(δηλ: int) -> Result:
                                if δηλ == len(list_of_numbers):
                                    return Result(δξη, βωτ)
                                else:
                                    def βπω(οπα: int) -> Result:
                                        return τυω(οπα + 1)

                                    def ακα(αβα: int) -> Result:
                                        return σθφ(αβα)

                                    def υξβ(υζθ: int) -> Result:
                                        return βπω(υζθ)

                                    return ακα(δηλ)

                            return ζψξ(0)

                    def τκβ(ωξθ: int) -> Result:
                        return τυω(ωξθ)

                    def ζβν(ζξδ: int) -> Result:
                        return τκβ(ζξδ)

                    return ζβν(ρνζ + 1)

            return σνξ(0)

    ρυν = αφύκ(0, None, None)

    return ρυν.pair