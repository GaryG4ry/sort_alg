def selectSort(inputData):
    length = len(inputData)
    if length == 0:
        return []

    for i in range(length):
        min_index = i
        for j in range(i + 1, length):
            if inputData[min_index] >= inputData[j]:
                min_index = j
        inputData[i], inputData[min_index] = inputData[min_index], inputData[i]
    return inputData


if __name__ == '__main__':
    l = [1, 2, 4, 8, 451, 33514, 512, 53, 44, 0, 2, 5]
    print(selectSort(l))
