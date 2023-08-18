def is_valid_walk(walk):
    n = 0
    s = 0
    w = 0
    e = 0
    print(walk)
    for i in walk:
        if i == "n":
            n += 1
            s -= 1
        if i == "s":
            s += 1
            n -= 1
        if i == "w":
            w += 1
            e -= 1
        if i == "e":
            e += 1
            w -= 1
    x = [n,s,e,w]
    if len(walk) != 10:
        return False
    for i in x:
        if i > 0:
            return False
        else:
            continue
    return True
