class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def CreateHeadNode(self, node):
        self.head = node

    def AddNode(self, node):
        currentNode = self.head
        while currentNode.next is not None:
            currentNode = currentNode.next
        currentNode.next = node

    def NodeExist(self, value):
        currentNode = self.head
        while currentNode.next is not value:
            currentNode = currentNode.next
            if currentNode is None:
                return False
        return True

    def InsertNode(self, value, node):
        currentNode = self.head
        while currentNode.next is not None:
            if currentNode.data == value:
                node.next = currentNode.next
                currentNode.next = node
                break
            currentNode = currentNode.next
        else:
            raise LookupError("Value does not exit in list")

    def RemoveNode(self, value):
        currentNode = self.head
        while currentNode.next is not None:
            if currentNode.next.data == value:
                currentNode.next = currentNode.next.next
                break
            currentNode = currentNode.next

    def RemoveALL(self, value):
        currentNode = self.head
        while currentNode.next is not None:
            if currentNode.next.data == value:
                currentNode.next = currentNode.next.next
            else:
                currentNode = currentNode.next

    def __str__(self):
        if self.head is not None:
            currentNode = self.head
            output = [currentNode.data]
            while currentNode.next is not None:
                output.append(currentNode.next.data)
                currentNode = currentNode.next
        return " -> ".join(map(str, output))


l = LinkedList()
l.CreateHeadNode(Node(9))
l.AddNode(Node(10))
l.AddNode(Node(8))
l.AddNode(Node(10))
l.AddNode(Node(10))
l.AddNode(Node(10))
l.AddNode(Node(9))
print(l)
l.RemoveALL(10)
print(l)
