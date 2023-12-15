#Assignment 1 Question


#importing deque module from collections ,it is used to create the double ended queue
from collections import deque
#defines a function reverse queue and takes  queue as a input and reverses it
def reverse_queue(queue):
#deque is imported from the collections,and dequeue stands for double ended queue,used to create a queue like structure where elements can be added or removed from both ends efficiently
    reversed_queue = deque()
    #enters a loop that continues untill input queue is empty
    while queue:
        #pop an element from the input queue and append it to the reverse queue
        reversed_queue.append(queue.pop())
        #return the reverse queue
    return reversed_queue

#created a function to handle multiple testcases
# Function to read input and process test cases
def process_test_cases():
    #reads the no of test cases as an integer
    num_test_cases = int(input())
    #iterates through each test case
    for _ in range(num_test_cases):
        #reads the no of elements from the queue for the current test case
        n = int(input())
        #reads space seperated elements as a string,maps them to integer, and stores them in a list named elements
        elements = list(map(int, input().split()))
#created a queue named queue using list of elements
        # Create a queue
        queue = deque(elements)

#calls the reverse queue function to reverese the queue elements
        # Reverse the queue
        reversed_queue = reverse_queue(queue)

#convert the elements in rversed queue to string,joins them with a spaces ,prints the resulting string
        # Output reversed queue
        print(' '.join(map(str, reversed_queue)))

#executes the function to process the test cases
# Run the function to process test cases
process_test_cases()


#the output is like 
# 1
# 6
# 1 2 3 4 5 10
