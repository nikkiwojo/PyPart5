from typing import List
from math import ceil
import math


def get_item_at_position(list_in: List, pos: int) -> List:
   return list_in[pos]


def print_list_items(list_in: List) -> None:
    for item in list_in:
        print(item)


def sort_by_commit_count(list_in: List) -> List:
    list_in.sort(key = lambda x : x[1])
    return list_in


def gen_list_of_nums(n: int) -> List[int]:
    numbers = []
    count = 0

    while n >= count+1:
        numbers.append(count)
        count += 1
    return numbers


def half_list(list_in: List, half: int) -> List:
    median_first = math.ceil(len(list_in)/2)
    median_second = len(list_in) // 2

    if half == 1:
        new_list = list_in[0:median_first]
    elif half == 2:
        new_list = list_in[median_second:]
    return new_list


def remove_odds(list_in: List[int]) -> None:
    for element in list_in:
        if element % 2 != 0:
            list_in.remove(element)

        print(list_in)


def remove_evens(list_in: List[int]) -> None:
   for element in list_in:
        if element % 2 == 0:
            list_in.remove(element)

        print(list_in)

def concatenate_lists(list_a: List, list_b: List) -> List:
    new_list = list_a + list_b
    return new_list


def multiply_list(list_in: List, scalar: int) -> List:
   new_list = list_in * scalar
   return new_list
