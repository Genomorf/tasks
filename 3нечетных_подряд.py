def is_3_numbers_odd(numbers: list) -> bool:
    counter: int = 0
    for number in numbers:
        if number % 2 != 0:
            counter += 1
        else:
            counter = 0
        if counter == 3:
            return True
    return False
