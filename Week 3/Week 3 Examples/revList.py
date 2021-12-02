from revIter import revLstIter

class revList(list):
    'a reverse list class'

    def __iter__(self):
        return revLstIter(self)
