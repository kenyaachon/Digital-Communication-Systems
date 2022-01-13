# template file for 6.02 PS1, Python Task 1
import PS1_tests
import heapq 

# arguments:
#   plist -- sequence of (probability,object) tuples
# return:
#   a dictionary mapping object -> binary encoding

class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

  def insert(self, char):
    if char == '(':
        if self.left is None:
            self.left = TreeNode(char)
        elif self.left.val == '(':
            self.left.insert(char)
        elif self.right is None:
            self.right = TreeNode(char)
        elif self.right.val == '(':
            self.right.insert(char)

    elif char == ')':
        if self.left.val == '(':
            self.left.insert(char)
        elif self.right.val == '(':
            self.right.insert(char)
        elif self.val == '(':
            self.val = self.val + char
    else:
        if self.left is None:
            self.left = TreeNode(char)
        elif self.left.val == '(':
            self.left.insert(char)
        elif self.right is None:
            self.right = TreeNode(char)
        elif self.right.val == '(':
            self.right.insert(char)
    
def printTree(root: TreeNode, encoding, encodingTree):
    if root is None:
        return 
    if root.left is None and root.right is None:
        print(encoding)
        encodingTree[root.val] = list(encoding)
        return


    printTree(root.left, encoding + "0", encodingTree)
    print(root.val)
    printTree(root.right, encoding + "1", encodingTree)



def createDictionary(pList):
    if len(pList) == 0:
        return {}

    encoding = {}
    symbols = pList.split(" ")
    root = TreeNode(symbols[0])
    for char in symbols[1:]:
        if char != '^':
            # print(char)
            root.insert(char)


    printTree(root, "", encoding)
    return encoding

def huffman(pList):
    """
    Example:
    plist: ((0.50,'A'),(0.25,'B'),(0.125,'C'),(0.125,'D'))
    returns: {'A': [0], 'B': [1, 0], 'C': [1, 1, 0], 'D': [1, 1, 1]} 
    """
    # Your Code Here
    tests = []
    for value in pList:
        heapq.heappush(tests, [value[0], value[1]])
    
    while len(tests) > 1:
        first = heapq.heappop(tests)
        second = heapq.heappop(tests)

        combinedProb = first[0] + second[0]
        symbol = '(' + " " + second[1] + " " + '^' + " " + first[1] +  " " + ')'

        heapq.heappush(tests, [combinedProb, symbol])
    # print(tests)

    return createDictionary(tests[0][1])

def main(plist):
    # encoding = "((J^X)^(Q^(A^K)))"
    # print(encoding.split("^"))
    # tests = huffman(plist)
    # print(createDictionary(tests[0][1]))
    print(huffman(plist))







if __name__ == '__main__':
    # main(((0.25,'A'),(0.25,'B'),(0.25,'C'), (0.25,'D')))


    main(((0.34,'A'),(0.5,'B'),(0.08,'C'),(0.08,'D')))
    # # test case 1: four symbols with equal probability

    # main(((0.25,'A'),(0.25,'B'),(0.25,'C'),(0.25,'D')))

    # main(((0.07,'I'),(0.23,'II'),(0.07,'III'), (0.38,'VI'),(0.13,'X'),(0.12,'XVI')))

    # PS1_tests.test_huffman(main,
    #                        # symbol probabilities
    #                        ((0.25,'A'),(0.25,'B'),(0.25,'C'),
    #                         (0.25,'D')),
    #                        # expected encoding lengths
    #                        ((2,'A'),(2,'B'),(2,'C'),(2,'D')))

    # # test case 2: example from section 22.3 in notes
    # PS1_tests.test_huffman(huffman,
    #                        # symbol probabilities
    #                        ((0.34,'A'),(0.5,'B'),(0.08,'C'),
    #                         (0.08,'D')),
    #                        # expected encoding lengths
    #                        ((2,'A'),(1,'B'),(3,'C'),(3,'D')))

    # # test case 3: example from Exercise 5 in notes
    # PS1_tests.test_huffman(huffman,
    #                        # symbol probabilities
    #                        ((0.07,'I'),(0.23,'II'),(0.07,'III'),
    #                         (0.38,'VI'),(0.13,'X'),(0.12,'XVI')),
    #                        # expected encoding lengths
    #                        ((4,'I'),(3,'II'),(4,'III'),
    #                         (1,'VI'),(3,'X'),(3,'XVI')))

    # # test case 4: 3 flips of unfair coin
    phead = 0.9
    plist = []
    for flip1 in ('H','T'):
        p1 = phead if flip1 == 'H' else 1-phead
        for flip2 in ('H','T'):
            p2 = phead if flip2 == 'H' else 1-phead
            for flip3 in ('H','T'):
                p3 = phead if flip3 == 'H' else 1-phead
                plist.append((p1*p2*p3,flip1+flip2+flip3))
    # expected_sizes = ((1,'HHH'),(3,'HTH'),(5,'TTT'))
    # PS1_tests.test_huffman(huffman,plist,expected_sizes)
    main(plist)