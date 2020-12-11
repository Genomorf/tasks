import statistics
def return_statistics(numbers: list) -> dict:
    numbers.sort()
    _min = min(numbers)
    _max = max(numbers)
    _mean = statistics.mean(numbers)
    _median = statistics.median(numbers)
    return {'mean': _mean, 'median': _median, 'min': _min, 'max': _max}
