from typing import List, Optional

def sort_array(UwX: List[int]) -> List[int]:
    def W35(L9: List[int]) -> List[int]:
        if not L9:
            return []
        G1 = W35(L9[1:])
        R0 = L9[0]

        def X3(P2: int, Q8: int, zZ: List[int]) -> List[int]:
            if not zZ:
                return [P2, Q8]

            Dv = zZ[0]

            def h8(E: int, Q: List[bool]) -> int:
                if not Q:
                    return E
                return h8(E * 2 + (1 if Q[0] else 0), Q[1:])

            def bits_as_bool_list(n: int) -> List[bool]:
                if n == 0:
                    # Represent zero as single False bit for consistency
                    return [False]
                bits_str = bin(n)[2:]  # binary string without '0b'
                return [c == '1' for c in bits_str]

            At = h8(0, bits_as_bool_list(Dv))
            AtP = h8(0, bits_as_bool_list(P2))

            if At < AtP:
                return X3(P2, Dv, zZ[1:])
            else:
                return X3(Dv, Q8, zZ[1:])

        # Handle the condition "[R0].concat(G1) == [None, None] ? [] : ..."
        # Since our lists are of int, None cannot be an element. We assume this condition is to handle empty or sentinel.
        # So we can ignore this check and always proceed to insertion.

        # Insert R0 into W35(L9.tail()) sorted by sum of bits of R0 and elements in list
        def insert_sorted(H: List[int]) -> List[int]:
            def bit_sum(n: int) -> int:
                bits = bits_as_bool_list(n)
                return sum(1 for b in bits if b)

            if not H:
                return [R0]
            if bit_sum(R0) <= bit_sum(H[0]):
                return [R0] + H
            else:
                return [H[0]] + insert_sorted(H[1:])

        return insert_sorted(W35(L9[1:]))

    return W35(UwX)