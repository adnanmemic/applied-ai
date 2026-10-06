def list_average(numlist: list[int | float]) -> float | None:
    if not numlist:
        return None

    return sum(numlist) / len(numlist)
