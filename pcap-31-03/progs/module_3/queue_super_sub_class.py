class QueueError(IndexError):
    pass


class Queue:
    def __init__(self):
        self.queue = []

    def put(self, elem):
        self.queue.insert(0, elem)

    def get(self):
        if len(self.queue) > 0:
            elem = self.queue[-1]
            del self.queue[-1]
            return elem
        else:
            raise QueueError

    def status(self):
        print(self.queue)


class SuperQueue(Queue):
    def __init__(self):
        Queue.__init__(self)

    def isempty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False


que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
que.status()

for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")
