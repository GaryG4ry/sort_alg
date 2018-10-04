class ShellSort:
    def __init__(self, inputData):
        self.inputData = inputData

    def shellSort(self):
        length = len(self.inputData)
        gap = length // 2
        while gap > 0:
            for i in range(gap, length):
                while i > gap and self.inputData[i] < self.inputData[i - gap]:
                    self.inputData[i], self.inputData[i - gap] = \
                        self.inputData[i - gap], self.inputData[i]
                    i = i - gap
            gap = gap // 2

        return self.inputData


if __name__ == '__main__':
    print(ShellSort([1, 5, 8, 565, 4, 2, 3, 44]).shellSort())
