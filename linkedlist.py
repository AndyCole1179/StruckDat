class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def push(self,newNode):
        #head => D->None
        if self.head == None:
            self.head = newNode

        else:
            lastNode = self.head
            while True:
                if lastNode.next == None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode
    
    def printList(self):
        currentNode = self.head
        while True:
            if currentNode == None:
                break
            print(currentNode.data)
            currentNode = currentNode.next

linkedList = LinkedList()
firstNode = Node("D")
linkedList.push(firstNode)
secondNode = Node("E")
linkedList.push(secondNode)
thirdNode = Node("S")
linkedList.push(thirdNode)
linkedList.printList()