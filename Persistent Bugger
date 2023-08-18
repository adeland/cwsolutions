def persistence(n):
    import math
    n = str(n)
    n = list(n)
    if len(n) == 1:
        return 0
    count = 0
    while len(n) != 1:
        count += 1
        for i in n:
            z = n.index(i)
            n[z] = int(n[z])

        n = math.prod(n)
        n = str(n)
        n = list(n)
        if len(n) == 1:
            return count
