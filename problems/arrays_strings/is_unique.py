import string

def is_unique_with_set(str_to_check: str) -> bool:
    visited_chars = set()
    for char in str_to_check:
        visited_chars.add(char)
    if len(visited_chars) == len(str_to_check):
        return True
    else:
        return False


def is_unique_without_set(str_to_check: str) -> bool:
    if len(str_to_check) <= 1:
        return True
    for char in str_to_check[1:]:
        if char == str_to_check[0]:
            return False
    return is_unique_without_set(str_to_check[1:])

def is_unique_with_ds(str_to_check: str) -> bool:
    """
    Correction
    We assume here that the the string is an ASCII string
    """
    if len(str_to_check) > len(string.printable):
        return False
    chars_found = [False for _ in range(128)]
    for char in str_to_check:
        if chars_found[ord(char)]:
            return False
        chars_found[ord(char)] = True
    return True
