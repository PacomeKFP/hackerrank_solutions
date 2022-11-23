def plusMinus(arr):
    positives_numbers = 0
    negatives_numbers = 0
    null_numbers = 0

    size = arr[0]
    array = [int(nbr) for nbr in arr[1].split()]
    for number in array:
        if number == 0:
            null_numbers += 1
        if number > 0:
            positives_numbers += 1
        if number < 0:
            negatives_numbers += 1

    print(f'{"%.6f"%(positives_numbers/size)}\n{"%.6f"%(negatives_numbers/size)}\n{"%.6f"%(null_numbers/size)}')
