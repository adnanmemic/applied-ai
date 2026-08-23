def list_average(numlist: list[float]) -> float | None:
    if not numlist:
        return None

    return sum(numlist) / len(numlist)