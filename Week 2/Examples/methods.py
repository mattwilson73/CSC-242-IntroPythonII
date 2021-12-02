class Super(object):
    def method(self):
        print('in Super.method')

class Sub(Super):
    def method(self):
        print('starting Sub.method')
        Super.method(self)
        print('ending Sub.method')


class Test:
    def __init__(self,value):
        self.value=value
        
    def method(self):
        return self.value
