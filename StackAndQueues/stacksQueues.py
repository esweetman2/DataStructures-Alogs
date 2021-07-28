## Stacks -- LIFO (Last in first out) -- push adds to top , pop removes from top
## Queues -- FIFO (First in first out) -- push adds to back , shift removes from front

#### STACK ######

# Inititalizes a Node for the stack
# default value is None 
class Node():
    def __init__(self, val = None):
        self.val = val
        self.next = None

## Initialize Stack with nothing in it
## LIFO (Last in first out)
class Stack():
    def __init__(self):
        self.top = None
        self.bottom = None
        self.len = 0

    ## Push on top of stack
    def push(self,val):
        # Create new Node
        new_node = Node(val)
        # If self.top is None that means stack is empty
        # So set top and bottom as new node 
        if self.top == None:
            self.top = new_node
            self.bottom = new_node

        # Else set temporary value as the top
        # Set new top as a new Node
        # Then set the next (Node under current Node) to the temporary node (old top) 
        else:
            temp = self.top
            self.top = new_node
            new_node.next = temp
        # print('node value ',new_node.val)

        # Increases the count of Stack
        self.len += 1
    

    # Remove from top of stack
    def pop(self):

        # If self.top is None, that means the stack is empty
        if self.top == None:
            print('Stack is empty')
            return 0

        # Set temporary variable as the current top    
        temp = self.top 

        # If top is None and bottom is None 
        # then only 1 Node in stack 
        if self.top == self.bottom:
            self.bottom = None
        
        # Set the top Node to the one below it
        self.top = self.top.next 

        # Decrese count
        self.len -= 1
        print(f'Removing {temp.val}')


    ## Displays the stack, starting at the top going down
    ## Left most value is the top in the print statement below
    def display(self):
        cur = self.top
        elems = []
        while cur != None:
            elems.append(cur.val)
            cur = cur.next
        print(elems)

    def length(self):
        print(f'The stack contains {self.len} elements')

stack = Stack()
stack.pop()
stack.push(1)
stack.push(2)
stack.length()
stack.display()
stack.pop()
stack.display()
stack.pop()
stack.length()
stack.display()

print('''

Now running Queue implementation

''')


#### Queue #####

## Initialize Queue Node
class Qnode():
    def __init__(self, val = None):
        self.val = val
        self.next = None

## Initialize the queue
## FIFO (First in first out)
class Queue():
    def __init__(self):
        self.front = None
        self.back = None
        self.len = 0
    
    '''
        Adds to front. If the front is None it means nothing is in the queue,
        so front and back are the new Node.
        Else there is a Node/ are Nodes in queue, so set the current back node's next value to the new Node
        then set the new back as the new Node 
    '''
    def enqueue(self,val):
        new_node = Qnode(val)
        if self.front == None:
            self.front = new_node 
            self.back = new_node 
        else:
            self.back.next = new_node
            self.back = new_node
        self.len += 1

    '''
    Removes from front of queue
    If front is empty, then the queue is empty.
    Else set front to the next in line.
    '''
    def dequeue(self):
        if self.front == None:
            print('The queue is empty')
        else:
            self.front = self.front.next
            self.len -= 1

    def length(self):
        print(f'This queue is {self.len} elements longs')
    
    # Display queue
    def display(self):
        cur = self.front
        elems = []
        while cur != None:
            elems.append(cur.val)
            cur = cur.next
        elems.reverse()
        print(elems)

q = Queue()

q.dequeue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
q.length()
q.display()
q.dequeue()
q.display()
q.dequeue()
q.display()
q.length()

