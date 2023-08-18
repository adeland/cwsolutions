def move_zeros(lst):
    count = 0
    for i in lst:
        if i == 0:
            count += 1
    if count == 0:
        return lst
    lst[:] = [x for x in lst if x != 0]
    if count != 0:
        while count != 0:
            lst.append(0)
            count -= 1
    return lst
        
