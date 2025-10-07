from collections import deque
from math import inf

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_node(values):
    lengthValues = len(values)
    index = 1
    if lengthValues <= 0:
        return None
    rootNode = TreeNode(val=values[0])
    processingQueue = deque()
    processingQueue.append(rootNode)
    while True:
        if not processingQueue:
            break
        currentNode = processingQueue.popleft()
        if index < lengthValues and values[index] is not None:
            childLeft = TreeNode(val=values[index])
            currentNode.left = childLeft
            processingQueue.append(childLeft)
        index += 1
        if index < lengthValues and values[index] is not None:
            childRight = TreeNode(val=values[index])
            currentNode.right = childRight
            processingQueue.append(childRight)
        index += 1
    return rootNode

def is_same_tree(p, q):
    if p is None and q is None:
        return True
    elif p is None or q is None:
        return False
    else:
        valuesEqual = not (p.val != q.val)
        if not valuesEqual:
            return False
        else:
            return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

class Solution:
    def minimumLevel(self, root):
        if root is None:
            return 0
        nodesQueue = deque([root])
        currentLvl = 1
        minSumValue = inf
        minimalLevel = 1
        while nodesQueue:
            nodeCount = len(nodesQueue)
            accumulatedSum = 0
            loopIndex = 0
            while loopIndex < nodeCount:
                currentNode = nodesQueue.popleft()
                accumulatedSum += currentNode.val
                if currentNode.left is not None:
                    nodesQueue.append(currentNode.left)
                if currentNode.right is not None:
                    nodesQueue.append(currentNode.right)
                loopIndex += 1
            if accumulatedSum < minSumValue:
                minSumValue = accumulatedSum
                minimalLevel = currentLvl
            currentLvl += 1
        return minimalLevel