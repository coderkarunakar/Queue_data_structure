class Node:
    def __init__(self,initData):
        
        self.data=initData
        self.next=None
        
class Queue:
    def __init__(self) -> None:
        self.__head=None
        self.__tail=None
        self.__count=0
    def enqueue(self,element):
        newNode=Node(element)
        #if the Queue is empty
        if self.__head is None:
            #both the head and tail start pointing to the new node
            self.__head = newNode
            self.__tail = newNode
            #if the Queue has some elements 
        else:
            #making next of tail as that new node 
            self.__tail.next = newNode
            #changing next to self.tail
            self.__tail = newNode
            #incrementing the count value
            self.__count = self.__count + 1

    def dequeue(self):
        if self.__head is None:
            print("Hey Queue is Empty")
            return
            #pointing head data
        data = self.__head.data
        #changing head pointer to next of its head
        self.__head = self.__head.next
        self.__count = self.__count-1
        return data



    def isEmpty(self):
        return self.size() == 0

    def size(self):
        return self.__count
    def front(self):
        #after completion of enqueue,dequeue it checks the head value (i.e first value)
        if self.__head is None:
            print("Hey the Queue is Empty")
            return
            #pointing the head data value
        data = self.__head.data
        return data