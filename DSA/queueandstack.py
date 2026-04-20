import queue
def queue_check(size):
    # From class queue, Queue is
    # created as an object Now L
    # is Queue of a maximum
    # capacity of 20
    L = queue.Queue(maxsize=size)

    # Data is inserted into Queue
    # using put() Data is inserted
    # at the end
    L.put(5)
    L.put(9)
    L.put(1)

    # get() takes data_gmt out from
    # the Queue from the head
    # of the Queue
    L.get()
    L.get()
    L.get()
    L.put([{2,3,4,5},44,45,0])
    L.put(27)
    print(L.get()[::-1])
    print(L.all_tasks_done)
    print(L.qsize())


class StackCheck:
    MAXSIZE = 4
    stack = [None] * MAXSIZE
    top = -1

    def __init__(self, max_size):
        self.MAXSIZE = max_size
        self.stack = [None] * max_size

    def isfull(s):
        if s.top == s.MAXSIZE - 1:
            return True
        else:
            return False

    def push(self, data):
        if not self.isfull():
            self.top = self.top + 1
            self.stack[self.top] = data
        else:
            print("Could not insert data_gmt, Stack is full.")
    def get_top(s):
        return s.top


if __name__ == '__main__':
    queue_check(6)
    x = StackCheck(7)
    # x.push(1)
    # x.push(1)
    # x.push(1)
    # x.push(1)
    # x.push(1)
    # print(x.stack)
    a = "dsasdas d"
    b = "dsasdas d"
    c = 155
    d = 257
    # print(a[1::-1])
    print(id(d) == id(257))
    print(x.get_top(),end="\n\n")