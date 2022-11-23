def countingSort(arr: 'list[int]'):
    frequences: list = [arr.count(i) for i in range(100)]
    sorted_list = []
    for i in range(len(frequences)):
        for j in range(frequences[i]):
            sorted_list.append(i)
    return sorted_list
