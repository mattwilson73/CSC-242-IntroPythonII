# a very simple queue class with exceptions added

class queue(object):
    def __init__(self):
        self.q = []
    def dequeue(self):
        if self.size() == 0:
            raise EmptyQueue("attempt to dequeue from an empty queue")
        return self.q.pop(0)
    def enqueue (self, item):
        return self.q.append(item)
    def size(self):
        return len(self.q)
    def isEmpty(self):
        return (self.size() == 0)
    def __repr__(self): # for the official string representation of queues
        return self.q.__repr__()
    def __str__(self): # for the unofficial string representation, like printing queue objects
        return 'none of your business'
    def __getitem__(self, key):
        if key >= len(self.q) or key <0:
            raise BadQueueIndexError()
        return self.q[key]
    def __setitem__(self, key, value):
        if key >= len(self.q) or key <0:
            raise BadQueueIndexError()
        self.q[key] = value
    def __iter__(self):
        return iter(self.q)

class BadQueueIndexError(Exception):
    pass

class EmptyQueue(Exception):
    def __init__(self, value = None):
        if value == None:
           self.v = "None"
        self.v = value
    def __str__(self):
        return repr(self.v)
