# class BinaryTree:
#     def __init__(self, rootObj):
#         self.key = rootObj
#         self.leftChild = None
#         self.rightChild = None
#
#     def insertLeft(self, newNode):
#         if self.leftChild == None:
#             self.leftChild = BinaryTree(newNode)
#         else:
#             t = BinaryTree(newNode)
#             t.leftChild = self.leftChild
#             self.leftChild = t
#
#     def insertRight(self, newNode):
#         if self.rightChild == None:
#             self.rightChild = BinaryTree(newNode)
#         else:
#             t = BinaryTree(newNode)
#             t.rightChild = self.rightChild
#             self.rightChild = t
#
#     def getRightChild(self):
#         return self.rightChild
#
#     def getLeftChild(self):
#         return self.leftChild
#
#     def setRootVal(self, obj):
#         self.key = obj
#
#     def getRootVal(self):
#         return self.key
#
#
# r = BinaryTree('a')
# print(r.getRootVal())
# print(r.getLeftChild())
# r.insertLeft('b')
# print(r.getLeftChild())
# print(r.getLeftChild().getRootVal())
# r.insertRight('c')
# print(r.getRightChild())
# print(r.getRightChild().getRootVal())
# r.getRightChild().setRootVal('hello')
# print(r.getRightChild().getRootVal())


class BinaryTree:
    def __init__(self, root):
        self.root = root
        self.leftChild = None
        self.rightChild = None

    def insertLeftChild(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRightChild(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def setRootVal(self, rootVal):
        self.root = rootVal

    def getRootVal(self):
        return self.root

    def getLeftVal(self):
        return self.leftChild

    def getRightVal(self):
        return self.rightChild


t = BinaryTree(1)
t.insertLeftChild(2)
t.insertRightChild(3)

print(t.getLeftVal().getRootVal())
print(t.leftChild)