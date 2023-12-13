#Inbuild stack and Queue in python
#stack (LIFO )similar to dynamic arrray
#Note:for inbuilt stack we can simply use  list but for Queue we cant use list


# #inbuilt stack as a list
# s=[1,2,3]
# s.append(4)
# s.append(5)

# print(s.pop())
# print(s.pop())
# print(s)

#we should not use list as a Queue in python because we can append O(1) it but we can not dequeue it 
#because  its gonna take O(n) operation



#inbuilt Queue

#creating an object of that class
import queue
q = queue.Queue()
#we have funcitonalities like put ,get,
q.put(1)
q.put(2)
q.put(3)
q.put(4)

#travel till queue becomes empty 
while not q.empty():
#put,get,empty is all its functionalities
    print(q.get())


print("this is for stack inbuilt")
#for stack (LIFO)
q = queue.LifoQueue()
q.put(1)
q.put(2)
q.put(3)

while not q.empty():
    print(q.get())