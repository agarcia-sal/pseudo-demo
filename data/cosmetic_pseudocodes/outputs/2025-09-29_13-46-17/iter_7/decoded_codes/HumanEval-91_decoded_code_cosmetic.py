from typing import List, Callable


def is_bored(zephyr72: str) -> int:
    import re

    # Helper recursive function to split input string into sentences and count those starting with "I "
    def recursn_t903(v9uNf: str) -> int:
        def splitter(s: str) -> List[str]:
            return re.split(r"[.?!]\s*", s)

        recursn_t903._splitter = splitter

        def helper(rzI9p: List[str]) -> int:
            if len(rzI9p) == 0:
                return rzI9p[0] if len(rzI9p) == 0 else 0  # (never reached due to prior if)
            return (1 if rzI9p[0].startswith("I ") else 0) + helper(rzI9p[1:])

        return helper(recursn_t903._splitter(v9uNf))

    # Tail-recursive style function for summing count of sentences starting with "I "
    def tail_recursive(acc: int, lst: List[int]) -> int:
        def f(self: Callable[..., int], acc: int, lst: List[int]) -> int:
            if not lst:
                return acc
            return self(self, acc + (1 if str(lst[0]).startswith("I ") else 0), lst[1:])
        return f(f, acc, lst)

    # First count of sentences starting with "I " using recursn_t903 returns count of sentences, not counts themselves
    # But in pseudocode, recursn_t903(zephyr72) returns int count, and this int is passed as lst to tail_recursive (which expects list)
    # So to maintain fidelity, we keep recursn_t903 returning int count of sentences starting "I "
    # Then the tail_recursive lambda adds again same count if the integer starts with "I "? This contradicts.

    # Pseudocode logic:
    # recursn_t903 splits input into sentences, for each sentence starting with "I " adds 1 recursively
    # Then tail-recursive lambda given acc=0, lst=recursn_t903(zephyr72) which is int -> this creates a problem since lst is int, 
    # but tail-recursive expects list
    # However, the pseudocode uses tail-recursive to process list of sentences similarly.
    # Possibly pseudocode is ambiguous; the best interpretation is that tail-recursive processes the list of sentences,
    # adding counts of sentences starting with "I " again.
    # So to solve this, we must make recursn_t903 return list of sentences (by re.split),
    # then tail_recursive processes this list counting sentences starting with "I "
    # but according to pseudocode:
    # recursn_t903 = lambda v9uNf: (lambda rzI9p: ( ... ))(recursn_t903._splitter(v9uNf))
    # and returns the sum as int, so it returns int directly. Then later:
    # return (lambda _ac, _xs: (lambda f: f(f, _ac, _xs)))(0, recursn_t903(zephyr72))
    # So recursn_t903(zephyr72) is passed as _xs param in tail-recursive function,
    # but tail-recursive function expects a list, from the code below it's expecting lst == [] check.

    # So, probably recursn_t903 returns list, i.e. recursn_t903 is counting sentences starting with "I " in a recursive way,
    # but the pseudocode returns int, but also the tail recursive expects list, implying recursn_t903 returns list.

    # To preserve the pseudocode faithfully, I will redefine recursn_t903 so 
    # it returns list of sentences split from input string, then tail-recursive function sums count 
    # of sentences starting with "I ".

    # But pseudocode defines recursn_t903 as recursive sum of 1 or 0 based on sentence starts with "I ", so the recursn_t903 returns int.
    # But then tail recursive again adds those counts from lst (which is recursn_t903(zephyr72), thus int), so tail-recursive gets lst=int, which is invalid.

    # The pseudocode logic looks like double counting.

    # To be faithful, implement exactly the pseudocode logic:
    # recursn_t903: returns int count of sentences starting with "I "
    # tail-recursive function applied with lst=recursn_t903(zephyr72), an int, treating as list (that would cause error)

    # So probably the pseudocode has a bug or the tail-recursive is reimplementing a count over the sentences too.

    # To preserve exact logic, implement recursn_t903 returning int,
    # then tail recursive adding either 1 or 0 to acc based on lst[0].slice(0, 2) == "I ", with lst being an int (so error)

    # Instead, interpret tail recursive as an independent process over the list of sentences, so supply it the split list of sentences.

    # So the final return is count of sentences starting with "I " (from tail-recursive sum over sentence list), where sentence list = recursn_t903._splitter(zephyr72)

    # Implement accordingly.

    sentences = re.split(r"[.?!]\s*", zephyr72)

    def tail_recursive_count(acc: int, lst: List[str]) -> int:
        def f(self: Callable[..., int], acc: int, lst: List[str]) -> int:
            if not lst:
                return acc
            return self(self, acc + (1 if lst[0].startswith("I ") else 0), lst[1:])
        return f(f, acc, lst)

    return tail_recursive_count(0, sentences)