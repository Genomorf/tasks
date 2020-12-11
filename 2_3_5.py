def find_2_3_5_number(n: int) -> int:
    if n == 0:
        return 0
    res: list = [1]
    num: int = 1
    while len(res) != n:
        num += 1
        if num % 2 == 0 or num % 3 == 0 or num % 5 == 0:
            res.append(num)
    return res[n-1]
