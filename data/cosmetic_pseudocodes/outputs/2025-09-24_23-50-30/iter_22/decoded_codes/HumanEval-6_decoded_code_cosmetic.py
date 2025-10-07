from typing import List

def parse_nested_parens(parens_seq: str) -> List[int]:
    def parse_paren_group(paren_cluster: str) -> int:
        depth_counter: int = 0
        highest_depth: int = 0
        idx: int = 0
        while idx < len(paren_cluster):
            sym: str = paren_cluster[idx]
            if sym == '(':
                depth_counter += 1
                if depth_counter > highest_depth:
                    highest_depth = depth_counter
            else:
                depth_counter -= 1
            idx += 1
        return highest_depth

    segments: List[str] = []
    start_idx: int = 0
    n: int = len(parens_seq)
    for idx in range(n + 1):
        if idx == n or parens_seq[idx] == ' ':
            if idx > start_idx:
                segments.append(parens_seq[start_idx:idx])
            start_idx = idx + 1

    results: List[int] = []
    for cluster in segments:
        results.append(parse_paren_group(cluster))
    return results