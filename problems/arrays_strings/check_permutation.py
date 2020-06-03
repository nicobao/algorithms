def are_permutations_sort(one_str: str, other_str: str) -> bool:
    one_str = "".join(sorted(one_str))
    other_str = "".join(sorted(other_str))
    if one_str != other_str:
        return False
    return True

def are_permutations(one_str: str, other_str: str) -> bool:
    one_str_counts = _calculate_counts(one_str)
    other_str_counts = _calculate_counts(other_str)
    if one_str_counts == other_str_counts:
        return True
    return False

def _calculate_counts(one_str):
    one_str_counts = dict()
    for char in one_str:
        if char not in one_str_counts:
            one_str_counts[char] = 1
        else:
            one_str_counts[char] = one_str_counts[char] + 1
    return one_str_counts
