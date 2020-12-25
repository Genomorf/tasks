def count_bottles(numBottles: int, numExchange: int) -> int:
    full_bottles: int = numBottles
    total_bottles: int = full_bottles
    empty_bottles: int = 0

    while full_bottles > 0:
        empty_bottles += full_bottles  # drink
        full_bottles = empty_bottles // numExchange  # convert empty to full
        total_bottles += full_bottles
        empty_bottles = empty_bottles - (full_bottles * numExchange)  # residue from conversion

    return total_bottles
