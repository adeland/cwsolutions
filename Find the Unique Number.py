def find_uniq(arr):
    if arr[0] == arr[1]:
        z = arr[0]
    if arr[0] != arr[1] and arr[1] != arr[2]:
        z = arr[0]
    else:
        z = arr[1]
    arr = list(filter(lambda x: x != z, arr))
    return arr[0]
