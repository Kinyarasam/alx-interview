#!/usr/bin/python3
def minOperations(target: int) -> int:
    """
    Computes the fewest number of operations needed to result
    in exactly n H characters.
    """
    if not isinstance(target, int) or target <= 0:
        # input check for positive integers
        return 0
    operations_count = 0
    copied_chars = 0
    total_chars = 1
    while total_chars < target:
        if copied_chars == 0:
            # init (the first copy all and paste)
            copied_chars = total_chars
            total_chars += copied_chars
            operations_count += 2
        elif target - total_chars > 0 and (
                target - total_chars) % total_chars == 0:
            # copy all and paste
            copied_chars = total_chars
            total_chars += copied_chars
            operations_count += 2
        elif copied_chars > 0:
            # paste
            total_chars += copied_chars
            operations_count += 1
    return operations_count
