from bitstring import BitArray #pip install bitstring

class Node(object):

    bits = None

    def __init__(self, val = 0, char = "", leftChild = None, rightChild = None):
        self.value = val
        self.character = char
        self.leftChild = leftChild
        self.rightChild = rightChild

class Queue:

    queue = []

    def __init__(self, text):
        for char in text:
            find = False
            for i in self.queue:
                if char == i.character:
                    i.value +=1
                    find = True
                    break
            if not find:
                self.queue.append(Node(1, char, ))
        self.sortMin()
        self.huffmanTree()

    def sortMin(self):
        tree = self.queue
        l = len(tree)
        for i in tree[::-1]:
            x =  tree.index(i)
            smallest = x
            leftChild = 2*x+1
            rightChild = 2*x+2

            if leftChild < l and tree[leftChild].value < tree[smallest].value:
                smallest = leftChild

            if rightChild < l and tree[rightChild].value < tree[smallest].value:
                smallest = rightChild

            if x != smallest:
                tree[x], tree[smallest] = tree[smallest], tree[x]


    def huffmanTree(self):
        while(len(self.queue) > 2):
            a = self.queue[0]
            self.queue[0] = self.queue.pop(-1)
            self.sortMin()

            b = self.queue[0]
            self.queue[0] = self.queue.pop(-1)
            self.sortMin()
            ab = Node(a.value + b.value, a.character + b.character, a , b)
            self.queue.append(ab)
            self.sortMin()

        a = self.queue[0]
        self.queue[0] = self.queue.pop(-1)
        self.sortMin()
        b = self.queue[0]
        ab = Node(a.value + b.value, a.character + b.character, a , b)
        self.queue[0] = ab


class huffmanDict:

    d = dict()

    def __init__(self, node, binString='0b'):
        if not node.leftChild is None:
            huffmanDict(node.leftChild, binString+'0')
        if not node.rightChild is None:
            huffmanDict(node.rightChild, binString+'1')
        if node.leftChild is None and node.rightChild is None:
            node.bits = BitArray(binString)
            self.d.update({node.character: node.bits})


def encode(text):
    cipher = ""
    for i in text:
        cipher += dictionary.d.get(i)
    return cipher


def decode(root, text):
    decoded = ""
    currNode = root
    for char in text:
        if char == '0':
            if currNode.leftChild.leftChild is None and currNode.leftChild.rightChild is None:
                decoded += currNode.leftChild.character
                currNode = root
            else:
                currNode = currNode.leftChild
        else:
            if currNode.rightChild.leftChild is None and currNode.rightChild.rightChild is None:
                decoded += currNode.rightChild.character
                currNode = root
            else:
                currNode = currNode.rightChild
    return decoded


with open("input.txt", "r") as inputtxt:
    string = inputtxt.read()
    huffmanTree = Queue(string).queue
    dictionary = huffmanDict(huffmanTree[0])
    cipher = encode(string)
    for i in dictionary.d:
        print(i, dictionary.d[i].bin)

with open("output.bin", "wb") as output:
    output.write(cipher.tobytes())


with open("output.bin", mode="rb") as output:
    bits = BitArray(output.read()).bin

with open("output.txt", "w") as outputtxt:
    outputtxt.write(decode(huffmanTree[0], bits))
