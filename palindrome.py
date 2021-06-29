def is_palindrome(value: str) -> bool:
    no_space = value.replace(" ", "")
    lower_case = no_space.lower()

    if lower_case[::-1] == lower_case:
        return True
    else:
        return False
