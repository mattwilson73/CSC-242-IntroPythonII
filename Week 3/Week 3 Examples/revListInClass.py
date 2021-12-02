from revIter import revLstIter

class revList(list):

    def __iter__(self):
        return revLstIter(self)
    
