from typing import Set, Callable


def is_multiply_prime(αXυ: int) -> bool:
    def is_prime(λΩ: int) -> bool:
        Λπ = 2

        def χψ(ζϪ: int) -> bool:
            return ζϪ == 0

        def recursive_check(ψβ: int) -> bool:
            if ψβ >= λΩ:
                return True
            if χψ(λΩ % ψβ):
                return False
            return recursive_check(ψβ + 1)

        return recursive_check(Λπ)

    def prime_set() -> Set[int]:
        ΣΓ: Set[int] = set()

        def gen_primes(δΞ: int) -> None:
            if δΞ > 100:
                return
            if is_prime(δΞ):
                ΣΓ.add(δΞ)
            gen_primes(δΞ + 1)

        gen_primes(2)
        return ΣΓ

    ΛΠ = sorted(prime_set())  # sort to allow index access

    def product_exists() -> bool:
        size = len(ΛΠ)

        def recur1(index1: int) -> bool:
            if index1 >= size:
                return False

            def recur2(index2: int) -> bool:
                if index2 >= size:
                    return recur1(index1 + 1)

                def recur3(index3: int) -> bool:
                    if index3 >= size:
                        return recur2(index2 + 1)
                    if ΛΠ[index1] * ΛΠ[index2] * ΛΠ[index3] == αXυ:
                        return True
                    return recur3(index3 + 1)

                return recur3(0)

            return recur2(0)

        return recur1(0)

    return product_exists()