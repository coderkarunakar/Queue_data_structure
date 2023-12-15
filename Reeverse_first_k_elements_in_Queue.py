from collections import deque

def reverse_first_k_elements(queue, k):
    #iterates upto k//2 times if it is 3//2 ==1 it 
    for i in range(k // 2):
        # Swaps the elements at corresponding positions to reverse the first k elements in the queue.
        #Main important logic:
        queue[i], queue[k - i - 1] = queue[k - i - 1], queue[i]

# Input parsing
n, k = map(int, input().split())
queue = deque(map(int, input().split()))

# Reverse the first K elements
reverse_first_k_elements(queue, k)


#by the above logic we will be able to get that form and in order  to print it we use this loop 
# Output the updated queue
#loops until queue is empty
while queue:
    #prints and removes the leftmost elements of the queue continuing until queue is empty
    print(queue.popleft(), end=" ")
