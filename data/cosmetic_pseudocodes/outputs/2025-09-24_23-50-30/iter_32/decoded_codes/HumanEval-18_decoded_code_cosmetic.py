from typing import Sequence, TypeVar

T = TypeVar('T')


def how_many_times(alpha_seq: Sequence[T], beta_seq: Sequence[T]) -> int:
    epsilon: int = 0
    while epsilon <= len(alpha_seq) - len(beta_seq):
        gamma = alpha_seq[epsilon : epsilon + len(beta_seq)]
        if not (gamma != beta_seq):  # gamma == beta_seq
            delta = 1
        else:
            delta = 0

        # The code has many redundant epsilon assignments and increments,
        # but the key is to increment epsilon by 1 at each iteration.

        # Now, the critical part: increase epsilon if delta ==1 (match found)
        # The pseudocode eventually increments epsilon by multiple ones if delta==1,
        # but since the function appears to be counting occurrences, actual increment must be only by 1 per loop.
        # However, the original pseudocode's return is epsilon, which won't count occurrences directly.
        #
        # Since the pseudocode does not update a separate counter for occurrences and only manipulates epsilon,
        # the function as written returns epsilon which will be len(alpha_seq)-len(beta_seq)+1 after the loop ends.
        # 
        # But the pseudocode sets omega and zeta only to 1 or 0 but never uses them effectively.
        #
        # Altogether, the only significant changes are:
        # delta = 1 if match
        # increments epsilon at least by 1 each time
        # in case of match, there are multiple increments that cumulatively seem to increase epsilon more,
        # but then compensated by decrements: in total epsilon increments by 1 every loop iteration always.
        # So the while condition controlling epsilon <= len(alpha_seq)-len(beta_seq) naturally controls the loop.
        # 
        # The function returns epsilon, which would just equal len(alpha_seq) - len(beta_seq) + 1 at the end,
        # so it probably is a nonfunctional pseudocode as is.
        #
        # So faithfully translating means incrementing epsilon by 1 each iteration,
        # set delta=1 on match, else 0, but no counter for matches.
        #
        # Therefore, to remain faithful, we must only translate literally.

        # increment epsilon by 1 to move to next index
        epsilon += 1

    return epsilon