#!/usr/bin/python3
"""finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """find peak of a list of unsorted integers"""

    if not list_of_integers:
        return None
    else:
        i = list_of_integers[0]
        for integers in range(1, len(list_of_integers)):
            if i < list_of_integers[integers]:
                i = list_of_integers[integers]
            else:
                continue
    return i
