def diagonalDifference(arr: list):
    array_size = arr[0]
    array = [[int(e) for e in arr[i].split()] for i in range(1, array_size+1)]
    print(array)
    s = 0
    for i in range(len(array)):
        s += array[i][i] - array[i][array_size-i-1]

    return s if s > 0 else -s
