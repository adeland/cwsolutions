def two_sum(numbers, target):
    x = {}
    for i, j in enumerate(numbers):
        y = target - j
        if y in x:
            return [x[y], i]
        x[j] = i
