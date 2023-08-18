def to_weird_case(words):
    x = list(words)
    c = -1
    z = -1
    for i in x:
        c += 1
        z += 1
        if i == ' ':
            c = -1
        if c % 2 == 0:
            x[z] = x[z].upper()
        if c % 2 == 1:
            x[z] = x[z].lower()
    x = "".join(x)
    return x
