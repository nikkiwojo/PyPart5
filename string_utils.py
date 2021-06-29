
def str_len(str_in: str) -> str:
    return len(str_in)


def first_char(str_in: str) -> str:
    return str_in[0]


def last_char(str_in: str) -> str:
    return str_in[-1]


def input_has_substring(str_in: str, sub_str_in: str) -> bool:
    if sub_str_in in str_in:
        return True
    else:
        return False


def substring(str_in: str, start: int, stop: int) -> str:
    return str_in[start:stop]


def opposite_case(str_in: str) -> str:
    return str_in.swapcase()




