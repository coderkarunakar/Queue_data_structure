#Queue using 2 stack:
#for theory explanation please refer note book


#logic:this is for enque as O(N) and dequeue as O(1) if you want viceversa simply make append in s1 and pop in s2 and now front also becomes O(n)so this approach is only good


#first move all elements from s1 to s2 and now s1 becomes empty 
#then insert an element into s1 and then 
#then move all the elements from s2 to s1

class QueueUsingTwoStacks:

    def __init__(self):
            #declaring 2 private stacks 
        self.__s1=[]
        self.__s2=[]
    def enqueue(self,data):
        #O(n) operation
        #travels until s1 len becomes 0
        while (len(self.__s1)!=0):
            #appending s1 values into s2 and values are poping from s1
            self.__s2.append(self.__s1.pop())
            #inserting an new element into s1
        self.__s1.append(data)

#again traveling untills2 becomes 0
        while (len(self.__s2)!=0):
            #appending s2 values into s1 and poping the elements from s2
            self.__s1.append(self.__s2.pop())
            # and finally return it 
        return


    def dequeue(self):
        #O(1) operation
        if (len(self.__s1)==0):
            return -1
            #simply removing last element of the stack
        return self.__s1.pop()
    def front(self):
        if (len(self.__s1)==0):
            return -1
        return self.__s1[-1]
    def size(self):
        return len(self.__s1)
    def isEmpty(self):
        return self.size() == 0


q=QueueUsingTwoStacks()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)

while(q.isEmpty() is False):
    print(q.front())
    q.dequeue()