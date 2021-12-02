import random
class Marble(object):

    def __init__(self):
        colors=['red','green','yellow','blue','grey','black']
        self.color = colors[random.randint(0,len(colors)-1)]

    def getColor(self):
        return self.color

class Jar(object):

    def __init__(self,marbles):
        self.marbles=marbles

    def getCount(self):
        return len(self.marbles)

    def getColors(self):
        lst=[]
        for marble in self.marbles:
            lst.append(marble.getColor())
        return lst

    def getColorCount(self,color):
        count =0
        for marble in self.marbles:
            if marble.getColor() == color:
                count+=1
        return count
                


marbles = []
for i in range(0,100):
    marbles.append(Marble())

j=Jar(marbles)
print(j.getColors())
print('Total red marbles : {}'.format(j.getColorCount('red')))        
