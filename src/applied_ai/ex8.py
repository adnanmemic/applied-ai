def list_average(numlist: list[int | float]) -> float | None:
    """Calculate the average of the numbers in a list.

    Args:
        numlist: List containing integers or floats.

    Returns:
        The average of the numbers, or None if the list is empty.
    """
    if not numlist:
        return None

    return sum(numlist) / len(numlist)
