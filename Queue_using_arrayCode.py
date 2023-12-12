# Queue using Array code
class QueueUsingArray:
    def __init__(self):
        #declaring an private array ,count initially it  is an empty list
        self.__arr = []
        self.__count = 0
        self.__front = 0
    def enqueue(self,data):
        #append the element into the array
        self.__arr.append(data)
        self.__count+=1
    def dequeue(self):

        #this  is also an O(1) operation
        #this means no element is present
        if self.__count==0:
            return -1
        #Note :when ever you delete an element you need to update front value,so front value is updtaed
        element =self.__arr[self.__front]
        self.__front+=1
        self.__count-=1

        return element
    def size(self):
        return self.__count
    


    def front(self):
        if  self.__count == 0:
            return -1
        return self.__arr[self.__front]
    def isEmpty(self):
        return self.size() == 0


        
q = QueueUsingArray()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
#that means there is an element in  Queue
while (q.isEmpty() is False):
    print(q.front())
    q.dequeue()
print(q.dequeue())