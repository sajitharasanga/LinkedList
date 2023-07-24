from main import Node


# create a doubly list
class linklist:  # head and tail
    def __init__(self):
        self.head = None  # head make as none
        self.tail = None  # tail make as none
        self.count = 0  # list length

    def listLength(self):
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.getNext()
        return count

    def printlistForword(self):  # create function to print list forward
        current = self.head
        if self.head is None:  # check if it is empty
            print("Empty linked list")  # if it is print"empty linked list"
        else:
            print("Nodes of doubly link list")
            while current is not None:  # create a loop until current is none
                print(current.getData())  # print value of node
                current = current.getNext()  # pointer go forwoard getting next node

    def printListBackword(self):  # create function to print list forward
        current = self.head
        if self.head is None:
            print("Empty Linked")
        else:
            print("Nodes of doubly link list")
            while current is not None:  # create a loop until current is none
                print(current.getData())  # print value of node
                current = current.previous()  # pointer go backwoard getting previous node

    def addNodeBegining(self, data):  # add a node to Begining of the list
        # create a new node
        newNode = Node()
        newNode.setData(data)

        if self.head is None:  # if list is empty
            self.head = self.tail = newNode  # head and tail will point to newNode
            self.head.previous = None  # head's previous will point to none
            self.tail.next = None  # tail's next will point to None
        else:  # Add newNode as new head of the list
            newNode.setNext(self.head)
            self.head.previous = newNode  # head's previous node will be newNode
            newNode.next = self.head  # newNode's next node will newNode
            newNode.previous = None  # newNode's previous will None
            self.head = newNode  # newNode will become new head

        self.length = 0

    def addNodeEnd(self, data):  # add a node to End of the list
        # create a new node
        newNode = Node()
        newNode.setData(data)

        if self.head is None:  # if list is empty
            self.head = self.tail = newNode  # head and tail will point to newNode
            self.head.previous = None  # head's previous will point to none
            self.tail.next = None  # tail's next will point to None
        else:
            current = self.head  # point to head Node
            while current.getNext() is not None:  # loop will over if list is empty
                current = current.getNext()
            current.setNext(newNode)  # current node will set as newNode
            newNode.setNext(None)  # self.length += 1 #list length increas adding one

    def addNodeInPos(self, pos, data):  # add the node to the given position
        if pos < self.length - 1 or pos < 0:  # check if position is in list length
            return None
        elif pos == 0:
            self.addNodeBeginning(data)
        elif pos == self.length - 1:
            self.addNodeEnd(data)  # if pos = list length -1 add Node the end
        elif pos == 0:
            self.addNodeBegining(data)  # if pos = 0 add node to the begining
        else:
            newNode = Node()  # creating new Node
            newNode.setData(data)
            count = 0  # creat a count variable
            current = self.head  # point to the head

            while count != pos - 1:  # if pos = count loop breaks
                count += 1  # untill it will increased by adding one
                current = current.getNext()  # get next reference
            newNode.setNext(current.getNext())  #
            current.setNext(newNode)  # current node will set newNode

    def delete_beging(self):  # creat function to delete the first node of the list
        if self.head is None:
            print("Empty link list")  # if it empty print "empty link list"
        else:
            self.head = self.head.getNext()  # head node will be next Nodes head
            self.head.self.setPreviouse(None)  # previouse element set as none
            self.length -= 1  # list length decrease by 1

    def deleteLastNode(self):  # function to delet a node in the end
        if self.head is None:
            print("empty Link list")  # if head node is empty print "empty link list"
        elif self.head != self.tail:  # check whether the list contain only one node
            self.tail = self.tail.previouse  # previous node to the tail will become new tail
            self.tail.next = None  # Node next to current tail will be made None
            self.length -= 1  # list lenght decrease by one

    def deleteNodeByPos(self, Pos):  # create function to delete node by position
        if self.head is None:
            print("Empty Link List")  # is list is empty print"Empty list"
            return None
        if self.length > Pos > -1:  # check list length > position > -1
            if Pos == self.length:
                self.deletelastNode()  # if pos equal list length delete last noce
            elif Pos == self.deleteLastNode - 1:
                self.deletelastNode()
            else:
                count = 0
                current = self.head  # create pointer to the head
                while count != Pos - 1:  # if count equal to the possiton loop break
                    count += 1  # until loop will increase by one
                    current = current.getNext()  # get next reference
                deletingNode = current.getNext()  # delete current Node  by next node
                nextNode = deletingNode.getNext()
                current.setNext(nextNode)
                self.length -= 1  # list lenth decresed by one

    def searchNode(self, value):  # search a given node
        i = 1
        flag = False
        current = self.head  # Node current will point to head
        if self.head == None:  # check whether the list is empty
            print("List is empty")
            return
        while current != None:
            if current.data == value:  # copare value search with node
                flag = True
                break  # if current equal to value loop break
            current = current.getNext  # untill loop countinue getting next node
            i = i + 1  # untill loop increse by one
        if flag:  # if value found print position
            print("Node's position in the list")
            print(i)
        else:  # if value doesnt found print" The Node isnt present in the list"
            print("The Node isnt present in the list ")

    def printing(self):  # print given position using printing node
        current = self.head
        if (self.head == None):
            print("The list is empty")
            return
        print("The node in doubly link list are :")
        while current != None:
            print(current.data)
            current = current.getNext

