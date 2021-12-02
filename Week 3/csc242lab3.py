'''Worked on during lab time with no direct collaborators'''

class Stat(object):
    'a stat class'
    
    def __init__(self,l=[]):
        'constructor accepting a list'
        self.l = l

    def sum(self):
        'sum of all values in Stat'
        try:
            return sum(self.l)
        except TypeError:
            return 'Error, non-number included in list'
        
    def max(self):
        'largest value in stat'
        try:
            return max(self.l)
        except ValueError:
            return 0.0
        
    def min(self):
        'smallest value in stat'
        try:
            return min(self.l)
        except ValueError:
            return 0.0
        
    def clear(self):
        'remove all items from stat'
        self.l.clear()
        
    def mean(self):
        'mean of all values in stat'
        if len(self.l) == 0:
            return 0.0
        else:
            return (self.sum() / len(self.l))
        
    def add(self,val):
        'add a value to Stat. must be a number'
        try:
            self.l.append(float(val))
        except ValueError:
            print('{} not added. Value must be a number.'.format(val))
        
    def __eq__(self,other):
        'returns True if the sum of the two Stat objects is equal'
        return self.sum() == other.sum()

    def __str__(self):
        'string representation of stat'
        return 'Stat object with {} items.'.format(len(self.l))

    def __repr__(self):
        'python representation of object'
        return 'Stat({})'.format(self.l)
    




