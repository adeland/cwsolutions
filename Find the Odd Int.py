def find_it(seq):
    if len(seq) == 1:
        return seq[0]
    elecount = {}
    for element in seq:
        if element in elecount:
            elecount[element] += 1
        else:
            elecount[element] = 1
    for key, value in elecount.items():
        x = value
        if x % 2 != 0:
            return key
