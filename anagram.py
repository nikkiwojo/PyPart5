def is_anagram(first_string: str, second_string: str) -> bool:
    no_space_first = first_string.replace(" ", "")
    no_space_second = second_string.replace(" ", "")

    alphabet_first = sorted(no_space_first)
    alphabet_second = sorted(no_space_second)

    if alphabet_first == alphabet_second:
        return True
    else:
        return False
