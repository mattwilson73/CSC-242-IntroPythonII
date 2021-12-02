class revLstIter(object):
    'the reverse list iterator class'

    def __init__(self, lst):
        'the constructor'
        self.ilst = lst
        self.index = len(lst) - 1

    def __next__(self):
        'the next method'
        if self.index <= -1:
            raise StopIteration()
        val = self.ilst[self.index]
        self.index -= 1
        return val
