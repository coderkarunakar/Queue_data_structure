from Queue_using_LL import Queue

q = Queue()
q.enqueue(1)
q.enqueue(5)
q.enqueue(3)
q.enqueue(14)

while q.isEmpty() is False:
    print(q.dequeue())
q.front()

