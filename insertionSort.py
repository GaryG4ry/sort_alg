class InsertionSort:
    def __init__(self, inputData):
        self.inputData = inputData
        print('original data:', self.inputData)

    def insertionSort(self):
        num = len(self.inputData)
        for i in range(1, num):
            temp = self.inputData[i]
            j = i - 1
            while j >= 0 and temp < self.inputData[j]:
                self.inputData[j + 1] = self.inputData[j]
                j -= 1
                self.inputData[j + 1] = temp
        return self.inputData

    def insertSort(self):
        for i in range(1, len(self.inputData)):
            temp = self.inputData[i]
            j = i - 1
            while j >= 0 and temp < self.inputData[j]:
                self.inputData[j + 1] = self.inputData[j]
                self.inputData[j] = temp
                j -= 1
        return self.inputData


if __name__ == '__main__':
    print(InsertionSort([1, 2, 5, 4, 7, 3]).insertionSort())
    print(InsertionSort([1, 2, 46, 8, 145, 66, 12]).insertSort())
