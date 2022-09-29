class PriorityQueue_List:
    def __init__(self):
        """constructor of the class object"""
        self.PQ_list = []
        if __name__ == '__main__':
            print("contructor was initiated")

    def __del__(self):
        """deconstructor of the class object"""
        self.PQ_list.clear()
        if __name__ == '__main__':
            print("Decontructor was initiated")

    def isEmpty(self):
        return self.PQ_list == []

    def size(self):
        return len(self.PQ_list)

    def enqueue(self, item):
        assert item == int or float, "value of the key element in the PQ has to be a number!"
        assert item >= 0, "value of the key element in the PQ cannot be ujemna!"
        self.PQ_list.insert(0, item)

    def dequeue_max(self):
        indexmax = 0
        PQsize = self.size()
        for i in range(1, PQsize):
            if self.PQ_list[i] > self.PQ_list[indexmax]:
                indexmax = i
        return self.PQ_list.pop(indexmax)

    def printPQ(self):
        i = 0
        print("elemnts in the queue:")
        while i < self.size():
            print("nr ", i, "=", self.PQ_list[i], '\t')
            i += 1
        if self.size() == 0:
            print("the queue is empty")


import random as rd

if __name__ == '__main__':
    print("***TEST OF THE IMPLEMENTATION***")
    print("***Implementation of a simple queue on a list:***")
    test_PQ_list = PriorityQueue_List()

    for i in range(20):
        PQkey = rd.randint(0, 400)
        test_PQ_list.enqueue(PQkey)

    test_PQ_list.printPQ()
    assert test_PQ_list.size() == 20, " the size fuction has issues"
    print("Size of the queue =", test_PQ_list.size(), '\n')

    while not test_PQ_list.isEmpty():
        print("handled element with the max key =", test_PQ_list.dequeue_max())


    assert test_PQ_list.isEmpty() == True, " dequeue_max function incorrectly deletes elements from the queue"
    print("Is the qeueu empty? ", test_PQ_list.isEmpty())

    print("\n\n***Attempting to handle element from an empty queue:***")
    test_PQ_list_2 = PriorityQueue_List()
    try:
        print("handled element with the max key =", test_PQ_list_2.dequeue_max())
    except IndexError:
        print("Queue is empty!")
