"""created 27.09.18"""


class Tree:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


    def isLeftChild(self):
        return self.left

    def isRightChild(self):
        return self.right

    def put(self, data):
        if data < self.data:
            if self.left is None:
                self.left = Tree(data)
            else:
                self.left.put(data)
        else:
            if self.right is None:
                self.right = Tree(data)
            else:
                self.right.put(data)

    def theMostLeft(self):
        if self.isLeftChild():
            self.left.theMostLeft()
        else:
            print(self.data)
    def theMostRight(self):
        if self.isRightChild():
            self.right.theMostRight()
        else:
            print(self.data)

    def preorderPrint(self):
        if self.data == 9:
            print(self.data )
        else:
            print( self.data)
        if self.left:

            self.left.preorderPrint()

        if self.right:
            self.right.preorderPrint()


x = Tree(9)
# x.put("a")
x.put(5)
x.put(4)
x.put(6)
x.put(12)
x.put(11)
x.put(13)
x.theMostLeft()
x.theMostRight()
# x.put("h")
# x.put("m")
# x.put("p")
# x.put("q")
x.preorderPrint()
