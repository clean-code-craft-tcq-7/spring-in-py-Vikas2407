
def calculateStats(numbers):
    if not numbers:
        return None  # or raise an exception if preferred

    n = len(numbers)
    total = sum(numbers)
    mean = total / n
    minimum = min(numbers)
    maximum = max(numbers)

    # Calculate variance and standard deviation
    variance = sum((x - mean) ** 2 for x in numbers) / n
    std_dev = variance ** 0.5

    return {
        'count': n,
        'sum': total,
        'mean': mean,
        'min': minimum,
        'max': maximum,
        'variance': variance,
        'std_dev': std_dev
    }
