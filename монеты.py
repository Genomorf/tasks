import itertools
def count_minimum_coins(coins: set, v: int) -> str:
    total_value: int = sum(coins)
    res_coins = ()
    if len(coins) == 1:
        if next(iter(coins)) >= v:
            res_coins = coins
    for amount_of_combinations in range(1, len(coins) + 1):
        combs = itertools.combinations(coins, amount_of_combinations)
        for combination in combs:
            if total_value >= sum(combination) and sum(combination) >= v:
                total_value = sum(combination)
                res_coins = combination
    return '{0} монеты{1}'.format(len(res_coins), res_coins)
