class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self, treeData=[]):
        self.root = self.constructTree(treeData)

    def constructTree(treeData):
        if len(treeData) == 0:
            return None
        else:
            nodeList = []
            nodeValList = []
            # for i in range(0, len(treeData)):
            #     if treeData[i, 0]


        

    #There's depth first search and breadth first search
    #within depth first, there's pre, in and post-order traversal
