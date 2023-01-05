#!/usr/bin/env python3
from typing import List


def canUnlockAll(boxes: List[List[int]]) -> bool:
    """Determines if all the boxes can be opened.

    A key with the same number as a box opens that box.
    You can assume all keys will be positive integers.
    There can be keys that do not have boxes.
    The first box boxes[0] is unlocked.

    Args:
        boxes (List[List[int]]): The list of boxes.

    Returns:
        bool: True if all boxes can be opened, else False.
    """
    # Keep track of which boxes we have keys for
    keys = set([0])

    # Iterate through the boxes and add their keys to the set
    for box in boxes:
        for key in box:
            keys.add(key)

    # Check if we have keys for all the boxes
    return all(key < len(boxes) for key in keys)
