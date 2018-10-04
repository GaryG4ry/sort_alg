class BubbleSort:

    def __init__(self, sortedList):
        self.sortedList = sortedList
        print('排序前的', self.sortedList)

    def bubbleSort(self):
        """
        对冒泡加入优化，如果某个轮次的比较没有发生数据交换，就说明数据已经有序，无需再进行比较
        :return:sorted list
        """
        if len(self.sortedList) == 0:
            return []
        for i in range(len(self.sortedList) - 1):
            exchange = False
            for j in range(len(self.sortedList) - 1):
                if self.sortedList[j] > self.sortedList[j + 1]:
                    self.sortedList[j + 1], self.sortedList[j] = \
                        self.sortedList[j], self.sortedList[j + 1]
                    exchange = True
            if not exchange:
                break
        print('排序后的', self.sortedList)
        return self.sortedList


obj = BubbleSort([1, 2, 5, 4, 7, 3]).bubbleSort()
