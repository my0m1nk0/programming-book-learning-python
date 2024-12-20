class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

print(Queue().size())
# Queue().enqueue(1)
# Queue().enqueue(2)
# Queue().enqueue(3)

p = Queue()
q = Queue()

print( p.size() == q.size())

# q.enqueue(6)
# q.enqueue('cat')
# q.enqueue(True)
# print(q.size())
# print(q.dequeue())
# print(q.dequeue())
# print(q.size())
