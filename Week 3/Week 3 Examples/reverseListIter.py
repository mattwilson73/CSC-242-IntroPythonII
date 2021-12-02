class revLstIter(object):
    'the reverse list iterator class'

    def __init__(self, lst):
        'the constructor'
        self.ilst = lst
        self.index = len(lst) - 1
        #print('CONSTRUCTOR!!', self.index)

    def __next__(self):
        'the next method'
        #print('STARTING NEXT')
        if self.index <= -1:
            raise StopIteration()
        val = self.ilst[self.index]
        #print('CURRENT INDEX', self.index)
        self.index -= 1
        #print('NEXT INDEX', self.index)
        return val

class revList(list):
    'a reverse list class'

    def __iter__(self):
        return revLstIter(self)
