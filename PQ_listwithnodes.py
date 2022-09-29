class Node:
    def __init__(self, initdata):
        """constructor of the class object"""
        assert initdata == int or float, "value of the element key in the node needs to be a number!"
        assert initdata >= 0, "value of the element key in the node cannot be less than 0!"
        self.data = initdata
        self.next = None

    def getData(self):
        """returns value of the element key in the node"""
        return self.data

    def getNext(self):
        """returns link to the next node"""
        return self.next

    def setData(self, newdata):
        """assigns new value of the element key in the node"""
        assert newdata == int or float, "value of the element key in the node needs to be a number!"
        assert newdata >= 0, "value of the element key in the node cannot be less than 0!"
        self.data = newdata

    def setNext(self, newnext):
        """assigns link to the new node"""
        self.next = newnext


class UnorderedList:
    def __init__(self):
        """constructor of the class object"""
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        """dolacza nowy element do listy"""
        assert item == int or float, "value of the element key in the node needs to be a number!"
        assert item >= 0, "value of the element key in the node cannot be less than 0"
        newnode = Node(item)
        newnode.setNext(self.head)
        self.head = newnode

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

    def search(self, item):
        assert item == int or float, "value of the wanted element key in the node needs to be a number!"
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self, item):
        assert item == int or float, "value of the element key in the node needs to be a number!"
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def get_max(self):
        current = self.head
        maxkey_value = -1
        while current != None:
            if current.getData() > maxkey_value:
                maxkey_value = current.getData()
            current = current.getNext()
        self.remove(maxkey_value)
        return maxkey_value

    def printlistwithnodes(self):
        current = self.head
        if current != None:
            while current != None:
                if current.getNext() != None:
                    print(current.getData(), end=" --> ")
                else:
                    print(current.getData())
                current = current.getNext()
        else:
            print("The list is empty!")


import random as rd

if __name__ == '__main__':
    print("***TEST OF THE IMPLEMENTATION***")
    print("***Implementation of a simple queue on a list with nodes:***")

    test_PQ_listwithnodes = UnorderedList()
    for i in range(20):
        PQkey = rd.randint(0, 400)
        test_PQ_listwithnodes.add(PQkey)

    test_PQ_listwithnodes.printlistwithnodes()
    assert test_PQ_listwithnodes.size() == 20, "the size fuction has issues"
    print("Size of the queue =", test_PQ_listwithnodes.size(), '\n')

    while not test_PQ_listwithnodes.isEmpty():
        print("handled element with the max key =", test_PQ_listwithnodes.get_max())

    assert test_PQ_listwithnodes.isEmpty() == True, "function get_max incorrectly deletes elements from the queue"
    print("IS the queue empty? ", test_PQ_listwithnodes.isEmpty())


    print("\n\n***Attempting to handle element from an empty queue:***")
    test_PQ_listwithnodes_2 = UnorderedList()
    try:
        print("handled element with the max key = =", test_PQ_listwithnodes.get_max())
    except AttributeError:
        print("Cannot access elements form the empty queue!")

