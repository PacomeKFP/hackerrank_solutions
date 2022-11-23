def miniMaxSum(arr):  # first method
    array: list = [int(nb) for nb in arr.split()]
    array.sort()
    mins = sum(array[0:4])
    maxs = sum(array[-4:])

    print(mins, ' ', maxs)
