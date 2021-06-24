from bitstring import BitArray #pip install bitstring

class Node(object):

    bits = None

    def __init__(self, val = 0, char = "", leftChild = None, rightChild = None):
        self.value = val
        self.character = char
        self.leftChild = leftChild
        self.rightChild = rightChild


def createTree(text):
    tree = []
    for char in text:
        find = False
        for i in tree:
            if char == i.character:
                i.value +=1
                find = True
                break
        if not find:
            tree.append(Node(1, char, ))
    sortMinTree(tree)
    huffmanTree(tree)
    return tree

def sortMinTree(tree):
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


def huffmanTree(tree):
    while(len(tree) > 1):
        a = tree[0]
        tree[0] = tree.pop(-1)
        sortMinTree(tree)

        b = tree[0]
        ab = Node(a.value + b.value, a.character + b.character, a , b)
        tree[0] = ab
        sortMinTree(tree)

def huffmanCodeTable(node, binString='0b'):
    if not node.leftChild is None:
        huffmanCodeTable(node.leftChild, binString+'0')
    if not node.rightChild is None:
        huffmanCodeTable(node.rightChild, binString+'1')
    if node.leftChild is None and node.rightChild is None:
        node.bits = BitArray(binString)
        huffmanTable.update({node.character: node.bits})

def encode(text):
    cipher = ""
    for i in text:
        cipher += huffmanTable.get(i)
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


input = open("input.txt", "r")
output = open("output.bin", "wb")

huffmanTable = dict()
string = input.read()
arr = createTree(string)
huffmanCodeTable(arr[0])
cipher = encode(string)

for i in huffmanTable:
    print(i, huffmanTable[i].bin)


output.write(cipher.tobytes())
input.close
output.close
